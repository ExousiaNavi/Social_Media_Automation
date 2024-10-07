import asyncio
import logging
import os
import json
import re

import urllib.parse
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from fake_useragent import UserAgent, FakeUserAgentError
from playwright.async_api import async_playwright
import mysql.connector
from mysql.connector import Error
from cryptography.fernet import Fernet, InvalidToken
from database.database import MySQLDatabaseHandler;
from en.password_encryptor import PasswordEncryptor
from decimal import Decimal
from spreedsheet.spreedsheet import GoogleSheetsManager
class TelegramBot:
    logging.basicConfig(level=logging.INFO)
    MAX_RETRIES = 5  # Maximum number of retries in case of error
    RETRY_DELAY = 5  # Delay between retries (in seconds)
    # logging.basicConfig(level=logging.INFO)
    def __init__(self):
        # Playwright browser setup
        self.sheet_id = ''
        self.page = None
        self.cookies = None
        self.xpaths_common = {
            'sign_in_button': '//button[contains(@class, "button_primary") and contains(text(), "Sign in")]',
            'sign_in_with_google': '//button[contains(@class, "button_secondary") and contains(text(), "Sign in with Google")]',
            'email_field': '//*[@id="identifierId"]',
            'email_next_button': '//*[@id="identifierNext"]/div/button/span',
            'password_field': '//*[@id="password"]/div[1]/div/div[1]/input',
            'password_next_button': '//*[@id="passwordNext"]/div/button/span',
            'login_confirm': '//nav/div[contains(@class, "logged-in")]',
            'just_browse': '//button[contains(text(), "Just browsing")]',
            'accept_all': '//button[contains(text(), "Accept all")]',
            'show_more_button': '//button[contains(text(), "Show more")]',
            'archive_button': '//a[contains(text(),"Go to the archive of posts")]',
            'archive_show_more_button': '//a[contains(text(), "Show more")]'
        }

        # self.BRANDS = {
        #     "Baji BDT": {
        #         "url": "https://telemetr.io/en/channels/1829680439-baji_bgd/publish",
        #         "sheet_id": '1V1aVnO_ShcEh5ZQG37DfYijdeS3rLkeyRb8Fn-xHeWk',
        #         "xpaths": {
        #             'show_more_button': '//button[contains(text(), "Show more")]',
        #             'archive_button': '//a[contains(text(),"Go to the archive of posts")]',
        #             'archive_show_more_button': '//a[contains(text(), "Show more")]'
        #         }
        #     }
        #     # Add other brands similarly
        # }

        self.service_account_file = 'path_to_your_service_account_file.json'
        self.db = MySQLDatabaseHandler(
                host="localhost",
                user="root",
                password="",  # Replace with your MySQL password, if any
                database="datasource"  # Replace with your database name
            )
        
         # Specify the paths to your credentials file and encryption key
        self.file_path = os.path.join("credentials", "credentials.json")
        self.key_file = os.path.join("encryption", "encryption_key.key")
        # Initialize the PasswordEncryptor with the paths to the JSON file and key file
        self.encryptor = PasswordEncryptor(self.file_path, self.key_file)
        
    
    async def run(self, email, password, main_url, currency, url, brand, ch_name, sheet_id):

        """Main wrapper to handle retries."""
        retries = 0
        while retries < self.MAX_RETRIES:
            try:
                await self.automate_task(email, password, main_url, currency, url, brand, ch_name, sheet_id)
                logging.info("Task completed successfully.")
                break  # Exit the loop if the task is successful

            except Exception as e:
                retries += 1
                logging.error(f"Error during task execution: {e}")
                if retries < self.MAX_RETRIES:
                    logging.info(f"Retrying... attempt {retries + 1}/{self.MAX_RETRIES}")
                    await asyncio.sleep(self.RETRY_DELAY * retries)  # Exponential backoff
                else:
                    logging.error(f"Max retries reached. Task failed after {self.MAX_RETRIES} attempts.")


     # Generate a key for encryption and decryption
    # You must store this key securely. Anyone with this key can encrypt and decrypt your data.
   
    # async def generate_key(self):
    #     return Fernet.generate_key()

    async def clean_number(self, value):
        """
        Clean the numeric string by removing non-numeric characters.
        
        :param value: The string value to clean.
        :return: The cleaned integer value.
        """
        try:
            # Remove any spaces or non-numeric characters (e.g., commas, spaces)
            clean_value = value.replace(" ", "").replace(",", "")
            logging.info(f"clean_value: {clean_value}")
            return int(clean_value)  # Convert to integer
        except ValueError as e:
            logging.error(f"Error converting '{value}' to int: {e}")
            return None  # Handle the error, return None, or handle it accordingly


    async def html_content(self, html, brand, currency):
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Select all div elements with a class that contains "container/post"
        cards = soup.select('div[class*="container/post"]')

        # Initialize an empty dataset list
        dataset = []
        post_id = 0
        # Loop through the selected cards
        for card in cards:
            # Extract the Telegram link
            telegram_link = card.select_one('.post-image a')
            link = telegram_link['href'] if telegram_link and telegram_link.has_attr('href') else 'No link found'
            # Extract the first number from the link using regex
            post_id = re.search(r'\d+', link)

            if post_id:
                post_id = post_id.group()  # Extract the matched number as a string
                logging.info(f"Post ID: {post_id}")
            else:
                logging.info("No Post ID found in the link")
             # Extract the post date
            date_element = card.select_one('div.flex.flex-wrap.items-center.justify-between.gap-x-4.gap-y-4 a')
            date_str = date_element.get_text(strip=True) if date_element else 'No date found'

            # Append the current year to the date string
            current_year = datetime.now().year
            # Initialize a variable to store the final date
            date_str_with_year = f"{date_str}, {current_year}"

            # Initialize a variable to store the final date
            formatted_date = date_str  # Default to the original string if conversion fails
        
            # Convert date string (e.g., "Sep 29, 04:28") into a datetime object
            try:
                post_date = datetime.strptime(date_str_with_year, '%b %d, %H:%M, %Y')
                # Check if the post date is in the future
                if post_date > datetime.now():
                    # Subtract one year if the date is in the future
                    post_date = post_date.replace(year=post_date.year - 1)
        
                formatted_date = post_date.strftime('%Y-%m-%d %H:%M')  # Format the date as YYYY-MM-DD HH:MM
            except ValueError:
                # If parsing fails, keep the original string
                formatted_date = date_str_with_year
            
            # Extract views (inside the span element after the eye icon)
            views_element = card.select_one('div.flex-1.items-baseline span:has(i.icon-eye-line)')
            views = views_element.get_text(strip=True) if views_element else 'No views found'

            # Extract reactions (e.g., 👍 and ❤ with counts) and calculate total reactions
            reactions = {}
            total_reactions = 0  # Initialize total reactions counter
            reaction_spans = card.select('div.flex.flex-wrap.gap-2 span.flex.items-center.gap-1')
            for span in reaction_spans:
                emoji = span.find('span').get_text(strip=True)  # Get the emoji (👍, ❤)
                count = span.get_text(strip=True).replace(emoji, '').strip()  # Get the count
                if count.isdigit():
                    count = int(count)  # Convert count to integer
                    reactions[emoji] = count
                    total_reactions += count  # Add to the total reactions

                
            logging.info(f"views: {views}, reactions: {total_reactions}")
            #insert to db
            data = {
                "brand": brand,
                "currency": currency,
                "post_id": post_id,
                "link": link,
                "date": formatted_date,
                "views": await self.clean_number(views),
                "reactions": total_reactions  # Add the total reactions
            }
            self.db.connect()
            self.db.insert_data('dataset','telegram_views_reactions', data)
            self.db.close()
            # Add to the dataset
            dataset.append({
                "brand": brand,
                "currency": currency,
                "post_id": post_id,
                "link": link,
                "date": formatted_date,
                "views": views,
                "reactions": total_reactions  # Add the total reactions
            })


        
        # Optionally print or return the dataset
        # print(dataset)
        channel_name = currency+'_'+"BsP"
        self.write_to_json(dataset, f'{channel_name}_post_data.json', brand)
        
        return dataset
    
    def convert_numeric_values(self, data):
        """
        Recursively convert Decimal types to int if possible, otherwise float.
        """
        if isinstance(data, dict):
            return {key: self.convert_numeric_values(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [self.convert_numeric_values(item) for item in data]
        elif isinstance(data, Decimal):
            # Convert to int if it's a whole number, otherwise to float
            return int(data) if data == int(data) else float(data)
        else:
            return data
    
    #send to google sheet
    
    async def automate_task(self, email, password, main_url, currency, url, brand, ch_name, sheet_id):
        """Main method to run Playwright automation."""
        async with async_playwright() as p:
            # Using fake-useragent to generate a random user agent for each session
            try:
                
                # self.db.connect()
                # dataset = self.db.fetch_and_categorize_posts_by_date('dataset','telegram_views_reactions')
                    
                # # Convert Decimals to float
                # # dataset_cleaned = self.convert_numeric_values(dataset)
                # # logging.info(f"Dataset: {dataset}")
                # await self.sendToSpreedsheet(dataset, sheet_id)
                
                ua = UserAgent()
                user_agent = ua.random
            except FakeUserAgentError:
                user_agent = user_agent
                logging.info("Using fallback user-agent due to fake-useragent error.")
            
            browser = await p.chromium.launch(
                headless=False,
                args=[
                    "--disable-blink-features=AutomationControlled",  # Disables detection of automation tools
                    "--disable-infobars",  # Disables "Chrome is being controlled by automated software" message
                    "--remote-debugging-port=9223",  # Changing default debugging port to avoid detection
                ]
            )
            context = await browser.new_context(
                user_agent=user_agent,
                viewport={"width": 1280, "height": 720},   # Set the same viewport size as your regular browser
                locale="en-US",                            # Set locale to match your regular browsing locale
                timezone_id="America/New_York"
            )
            
            # Add stealth scripts to avoid detection
            await context.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
                Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
                Object.defineProperty(navigator, 'platform', { get: () => 'Win32' });
                WebGLRenderingContext.prototype.getParameter = function(parameter) {
                    if (parameter === 37445) return 'Intel Inc.';
                    if (parameter === 37446) return 'Intel Iris OpenGL Engine';
                    return WebGLRenderingContext.prototype.getParameter(parameter);
                };
            """)

            self.page = await context.new_page()

            logging.info(f"Processing {currency}...")

            await self.page.goto(main_url)
            logging.info("Navigating to the website...")

            
            logging.info(f"Encrypting Password: {password}")
            
            # Decrypt the password using the loaded key
            decrypted_password = self.encryptor.decrypt_password(password)
            logging.info(f"Decrypting Password: {decrypted_password}")
            # Perform login
            try:
                await self.page.locator(self.xpaths_common['sign_in_button']).nth(0).click()
                await self.page.click(self.xpaths_common['sign_in_with_google'])
                await self.page.fill(self.xpaths_common['email_field'], email)
                await self.page.click(self.xpaths_common['email_next_button'])
                await self.page.fill(self.xpaths_common['password_field'], decrypted_password)
                await self.page.click(self.xpaths_common['password_next_button'])
                logging.info("Logged in successfully.")
                await asyncio.sleep(10)
                    
                # Extract cookies after login
                cookies = await context.cookies()
                self.cookies = cookies 
            except Exception as e:
                logging.error(f"Login failed: {e}")
                raise  # Re-raise to trigger retry

            # Navigate to the channel URL
            await self.page.goto(url, timeout=50000)
            logging.info(f"Navigated to {url}")
            await asyncio.sleep(10)
            # await self.page.locator(self.xpaths_common['just_browse']).click(force=True)
            await self.page.locator(self.xpaths_common['accept_all']).click(force=True)
            # Click "Show More"
            await self.click_show_more(self.xpaths_common['show_more_button'], 3, 'out', currency, brand, ch_name,sheet_id)
                
            await self.page.click(self.xpaths_common['archive_button'])
               
            # Wait for the navigation to complete after the click
            await self.page.wait_for_load_state('networkidle')  # Wait until network is idle to ensure full page load

            
            
            await asyncio.sleep(2)
            await self.click_show_more(self.xpaths_common['archive_show_more_button'], 5, 'in', currency, brand, ch_name,sheet_id)
            
            # Get the new page's HTML content
            html_contents = await self.page.content()

            dataset = await self.html_content(html_contents, brand, currency)
                
                
            #send to spreedsheet
            self.db.connect()
            dataset = self.db.fetch_and_categorize_posts_by_date('dataset','telegram_views_reactions', brand, currency)
                
            # # Convert Decimals to float
            # dataset_cleaned = self.convert_numeric_values(dataset)
            # logging.info(f"Dataset: {dataset_cleaned}")
            await self.sendToSpreedsheet(dataset, sheet_id)
                    
            # # channel_name = currency+'_'+cursor_value
            # self.write_to_json(filtered_response, f'dataset_post_data.json', brand)
            self.db.close()    
                
            # Extract posts data
            # post_data = await self.extract_dynamic_post_ids()

            # Write data to JSON
            # self.write_to_json(post_data, f'{channel_name}_post_data.json')

            await browser.close()
    
    
    # Function to format the publish date
    def format_publish_date(self,date_str):
        # date_obj = datetime.fromisoformat(date_str[:-1])  # Remove the 'Z' for parsing
        # return date_obj.strftime("%b %d, %Y")  # Format to "Sep 19, 2024"
        # Parse the date
        parsed_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")

        # Format the date
        formatted_date = parsed_date.strftime("%Y-%m-%d %H:%M")
        return formatted_date
    
    # Function to remove unwanted fields from each message
    async def filter_response(self, data, fields, brand, currency, ch_name):
        filtered_messages = []
        dataset = []
        for message in data['messages']:
            filtered_message = {k: v for k, v in message.items() if k not in fields}
            try:
                dataset = {
                    "brand": brand,
                    "currency": currency,
                    "date": self.format_publish_date(filtered_message['meta']['publishDate']),
                    "post_id": filtered_message['messageId'],
                    "link": f"{ch_name}/{filtered_message['messageId']}",
                    "views": filtered_message['meta']['views'],
                    "reactions": filtered_message['meta']['reactionsCount']
                }
                
                
                #insert to database
                self.db.connect()
                self.db.insert_data('dataset','telegram_views_reactions', dataset)
                self.db.close()
                
                filtered_messages.append(dataset)
                
                
                
            except Exception as e:
                logging.error(f"Dataset Problem: {e}")
                break
            # logging.info(f"Dataset: {filtered_messages}")
        return {"messages": filtered_messages}

    async def sendToSpreedsheet(self, data, sheet_id):
        # Loop over the tuple data
        for post in data:
            try:
                # Unpack each tuple to extract values
                post_id, date, brand, currency, total_views, total_reactions, days_since_posted, days_string = post

                # Check if days_since_posted is 3, 7, or 30
                if days_since_posted in [3, 7, 30]:
                    # Ensure total_views and total_reactions are floats (not Decimal)
                    total_views = float(total_views) if isinstance(total_views, Decimal) else total_views
                    total_reactions = float(total_reactions) if isinstance(total_reactions, Decimal) else total_reactions

                    # Convert post_id to a string or float if it's a Decimal
                    post_id = str(post_id) if isinstance(post_id, Decimal) else post_id

                    # Convert days_string to str, and make sure it isn't a Decimal
                    days_string = str(days_string) if isinstance(days_string, Decimal) else days_string

                    # Debugging: Check after conversion
                    logging.info(f"Converted post_id: {post_id}, days_string: {days_string}")

                    # Print or process the post data
                    logging.info(f"Processing Post ID: {post_id}, Date: {date}, Views: {total_views}, Reactions: {total_reactions}, Days Since Posted: {days_since_posted}")

                    # Initialize GoogleSheetsManager
                    gmanager = GoogleSheetsManager(
                        'gs.json',  # Adjust path if needed
                        ["https://www.googleapis.com/auth/spreadsheets"],
                        sheet_id,  # Spreadsheet ID
                        'Telegram',  # Worksheet name
                        [total_views, total_reactions],  # Example BO data
                        days_string,  # Keyword to search for
                        'POST LINK',  # Target column to update
                        str(post_id)  # Post ID to search and update in the sheet
                    )

                    # Run the GoogleSheetsManager task
                    status = await gmanager.run()
                    if status['status'] == 200:
                        logging.info(f"Automation status: {status['post_id']}")
                    else:
                        logging.error(f"Automation failed with status: {status}")

                else:
                    logging.info(f"Skipping Post ID: {post_id}, Days Since Posted: {days_since_posted}, not in [3, 7, 30]")

            except Exception as e:
                logging.error(f"Error processing post ID {post_id}: {e}")
                # Optionally, you can continue to the next post or handle retry logic here
                continue
   
                    
    async def sendApiRequest(self, cursor, currency, brand, ch_name, sheet_id):
        
                # Parse the URL
                parsed_url = urllib.parse.urlparse(cursor)

                # Extract the query parameters
                query_params = urllib.parse.parse_qs(parsed_url.query)

                # Get the value of the 'cursor' parameter
                cursor_value = query_params.get('cursor', [None])[0]
                # Convert Playwright cookies to a format compatible with requests
                cookies_dict = {cookie['name']: cookie['value'] for cookie in self.cookies}
                # logging.info(f"Cookies: {cookies_dict}")
                    
                # Now use requests to send the POST request with the extracted cookies
                url = 'https://gw-prod.telemetr.io/store.v1.Messages/ChannelMessages'
                payload = {
                        "channel": {"telegramId": "1829680439"},
                        "returnShortInfo": True,
                        "cursor": cursor_value
                }

                headers = {
                    'Accept-Encoding': 'gzip, deflate, br, zstd',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'Content-Length': '78',
                    'Host': 'gw-prod.telemetr.io',
                    'Origin': 'https://telemetr.io',
                    'Referer': 'https://telemetr.io/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
                    'accept': 'application/json',
                    'content-type': 'application/json',
                    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }


                # Send the POST request with cookies
                response = requests.post(url, json=payload, headers=headers, cookies=cookies_dict)

                # logging.info(f"Response: {response.status_code}, {cursor_value}")
                # Define the fields you want to remove
                fields_to_remove = ['channel', 'message', 'mediaRaw', 'entities', 'album', 'photo', 'video', 'isAd','emoticon','deletedAt','forwardsCount']
                # Filter the response
                filtered_response = await self.filter_response(response.json(), fields_to_remove, brand, currency, ch_name)
                    
                channel_name = currency+'_'+cursor_value
                self.write_to_json(response.json(), f'{channel_name}_post_data.json', brand)
                    
                    
                # #send to spreedsheet
                # self.db.connect()
                # dataset = self.db.fetch_and_categorize_posts_by_date('dataset','telegram_views_reactions')
                
                # # Convert Decimals to float
                # dataset_cleaned = self.convert_numeric_values(dataset)
                # logging.info(f"Dataset: {dataset_cleaned}")
                # await self.sendToSpreedsheet(dataset_cleaned, sheet_id)
                    
                # # # channel_name = currency+'_'+cursor_value
                # self.write_to_json(filtered_response, f'dataset_post_data.json', brand)
                # self.db.close()      
                        
                            
    async def click_show_more(self, show_more_xpath, clicks, t, currency, brand, ch_name,sheet_id):
        """Click the 'Show More' button multiple times."""
        for i in range(clicks):
            try:
                # Scroll the element into the viewport before clicking
                show_more_button = self.page.locator(show_more_xpath)
                await show_more_button.scroll_into_view_if_needed()
                
                if(t == 'in'):
                     # Sometimes buttons might have hrefs if they act like links, or the parent element might have it.
                    href = await show_more_button.get_attribute('href')

                    if href:
                        print(f"Found href: {href}")
                        # await self.sendApiRequest(href, currency, brand, ch_name,sheet_id)
                        
                        
                    else:
                        print("No href found for this button.")
                await show_more_button.click(force=True)
                logging.info(f"Clicked 'Show More' {i+1} time(s).")
                await self.page.wait_for_timeout(2000)  # Wait 5 seconds between clicks
            except Exception as e:
                logging.error(f"Error clicking 'Show More': {e}")
                break

    def write_to_json(self, data, filename, brand):
        # Define the base folder path
        folder_path = "baji_json_folder"
        
        # Create a sub-folder based on the brand name
        sub_folder = os.path.join(folder_path, brand)
        
        # Create the base folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Create the sub-folder (brand folder) if it doesn't exist
        if not os.path.exists(sub_folder):
            os.makedirs(sub_folder)
        
        # Define the full file path inside the brand sub-folder
        full_path = os.path.join(sub_folder, filename)
        
        try:
            # Write the JSON data to the file
            with open(full_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
                logging.info(f"Data written to {full_path}")
        except Exception as e:
            logging.error(f"Error writing data to JSON file {full_path}: {e}")
# # To run the bot
# if __name__ == "__main__":
#     bot = TelegramBotPlaywright()
#     asyncio.run(bot.automate_task())
