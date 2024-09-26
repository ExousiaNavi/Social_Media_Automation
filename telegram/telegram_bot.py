import logging
import time
# from scraper import WebScraper
# from data_handler import DataHandler
# from config import BRANDS
import os
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from selenium import webdriver
from utilities.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import re
from selenium.webdriver.chrome.service import Service
import mysql.connector
from mysql.connector import Error


# This class contains the Selenium actions to automate Telegram Web
class TelegramBot:
    def __init__(self):
         # Get the Selenium WebDriver instance from the Browser class
        self.driver_path = r'C:\Users\BJ-LAP-65\Documents\GitHub\Social_Media_Automation\chromedriver-win64\chromedriver.exe'
        # self.channel_url = ''
        self.sheet_id = ''
        self.driver = ''
        # self.driver = Browser().get_driver()

        # MySQL Database configuration
        self.db_config = {
                'host': 'localhost', # Replace with your MySQL host
                'user': 'root',  # Replace with your MySQL username
                'password': '',  # Replace with your MySQL password
                'database': 'datasource'  # Replace with your MySQL database
            }

        self.conn = None
        self.cursor = None
        self.connect_to_db()

    def connect_to_db(self):
                """Establish a connection to the MySQL database."""
                try:
                    self.conn = mysql.connector.connect(**self.db_config)
                    if self.conn.is_connected():
                        self.cursor = self.conn.cursor()
                        # self.create_table()
                        print("Connected to the database.")
                except Error as e:
                    print(f"Error connecting to MySQL: {e}")

                self.email = "paulabutar7@gmail.com"
                self.password = "Bernerslee11"
                self.xpaths_common = {
                'sign_in_button': '/html/body/header/nav/div[5]/button',
                'sign_in_with_google': '//*[@id="headlessui-dialog-panel-:r5:"]/div/div[1]/div/button[2]',
                'email_field': '//*[@id="identifierId"]',
                'email_next_button': '//*[@id="identifierNext"]/div/button/span',
                'password_field': '//*[@id="password"]/div[1]/div/div[1]/input',
                'password_next_button': '//*[@id="passwordNext"]/div/button/span',
                'login_confirm': '/html/body/header/nav/div[5]'
            }   
                self.BRANDS = {
                    # Commented out BDT, INR, and NPR for testing PKR
                    "Baji BDT": {
                        "url": "https://telemetr.io/en/channels/1829680439-baji_bgd/publish",
                        "sheet_id": '1V1aVnO_ShcEh5ZQG37DfYijdeS3rLkeyRb8Fn-xHeWk',
                        "xpaths": {
                            'show_more_button': "/html/body/main/div[6]/div[2]/div[2]/div[2]/div/button",
                            'archive_button': "/html/body/main/div[6]/div[2]/div[2]/div[2]/div/a",
                            'archive_show_more_button': "/html/body/main/div[6]/div[2]/div/button"
                        }
                    },
                    "Baji INR": {
                        "url": "https://telemetr.io/en/channels/1545322793-baji_ind",
                        "sheet_id": '17cyuRgQ0zj4C3XGboHdJ-GAr8Vm09TOgqaM_NkQc92I',
                        "xpaths": {
                            'show_more_button': "/html/body/main/div[6]/div[1]/div[2]/div/button",
                            'archive_button': "/html/body/main/div[6]/div[1]/div[2]/div/a",
                            'archive_show_more_button': "/html/body/main/div[6]/div[2]/div/button"
                        }
                    },
                    "BAJI PKR": {
                        "url": "https://telemetr.io/en/channels/1803180364-baji_pak",
                        "sheet_id": '1tn4Fa6-etkqyYvnQYp-pULjr_AH2ZWWUXyxVBEzGXko',
                        "xpaths": {
                            'show_more_button': "/html/body/main/div[6]/div[1]/div[2]/div/button",
                            'archive_button': "/html/body/main/div[6]/div[1]/div[2]/div/a",
                            'archive_show_more_button': "/html/body/main/div[6]/div[2]/div/button"
                        }
                    },
                    "BAJI NPR": {
                        "url": "https://telemetr.io/en/channels/2058296847-baji_npl",
                        "sheet_id": '1ufiXUw3lyvHUnnLPRE7ZA_gTIaTVExmNEIyEZcxBOiU',
                        "xpaths": {
                            'show_more_button': "/html/body/main/div[6]/div[1]/div[2]/div/button",
                            'archive_button': "/html/body/main/div[6]/div[1]/div[2]/div/a",
                            'archive_show_more_button': "/html/body/main/div[6]/div[2]/div/button"
                        }
                    }
                }

                self.service_account_file = r"C:\Users\BJ-LAP-65\Documents\GitHub\Social_Media_Automation\all-brands-performance-3711739d3e51.json"

    # Method to open Telegram Web using Selenium
    def automate_task(self, max_retries=3, retry_delay=5):
            print("Opening Telegram web...")
        # Navigate to Telegram Web
        # self.driver.get("https://web.telegram.org")
            try:
                for channel_name, channel_info in self.BRANDS.items():
                    # Create a driver
                    self.driver = self.create_driver()
                    logging.info(f"Processing {channel_name}...")
                    self.sheet_id = channel_info['sheet_id']

                    # If no cookies or expired session, log in manually
                    time.sleep(3)
                    self.driver.get("https://telemetr.io/en")
                    print("Navigating to the website...")
                    # Click the elements to login
                    self.click_element(self.xpaths_common['sign_in_button'])
                    time.sleep(3)
                    self.click_element(self.xpaths_common['sign_in_with_google'])
                    # Input email and password
                    time.sleep(3)
                    self.input_text(self.xpaths_common['email_field'], self.email)
                    time.sleep(3)
                    self.click_element(self.xpaths_common['email_next_button'])
                    time.sleep(5)
                    self.input_text(self.xpaths_common['password_field'], self.password)
                    time.sleep(5)
                    self.click_element(self.xpaths_common['password_next_button'])
                    time.sleep(5)
                    # Wait for manual login
                    self.wait_for_manual_login(self.xpaths_common['login_confirm'], channel_info['url'])
                    # Save cookies after successful login
                
                    # Continue with the rest of your scraping process
                    xpaths_channel = channel_info['xpaths']
                        
                    # Use the correct modal XPaths based on the brand
                    # xpaths_modals = {
                    #     "first_xbutton_modal": "/html/body/main/div[6]/div[2]/div/div/div[2]/div[2]/button",  # Example XPath
                    #     "second_xbutton_modal": "/html/body/main/div[6]/div[2]/div/div/div[2]/div[3]/i"       # Example XPath
                    # }
                    # //*[@id="headlessui-dialog-panel-:r72:"]/div[1]/div[1]/button/i
                    #     //*[@id="headlessui-dialog-panel-:r74:"]/div/div[3]/i
                    xpaths_modals = {
                        "first_xbutton_modal": "//*[starts-with(@id, 'headlessui-dialog-panel')]/div[1]/div[1]/button",  # Example XPath
                        "second_xbutton_modal": "//*[starts-with(@id, 'headlessui-dialog-panel')]/div/div[3]/i"       # Example XPath
                    }
                        
                    # Click "Show More" and close modals if they appear
                    self.click_show_more(xpaths_channel['show_more_button'], xpaths_modals, clicks=3)
                    print("Clicked 'Show More' on the main page...")
                    
                    self.click_element(xpaths_channel['archive_button'])
                    print("Clicked on the Archive button...")

                    self.click_show_more(xpaths_channel['archive_show_more_button'], xpaths_modals, clicks=5)
                    print("Clicked 'Show More' in the Archive page...")

            
                    post_data = self.extract_dynamic_post_ids()

                    # Print the extracted post data for visibility
                    print(f"Extracted post data for {channel_name}:")
                    # for post in post_data:
                    #     print(post) 
                    self.write_to_json(post_data, f'{channel_name}_post_data.json')
                    self.upload_to_google_sheets(post_data)

                    logging.info(f"Completed processing for {channel_name}\n")
                    self.driver.quit()

            except Exception as e:
                    logging.error(f"Error processing automation task {channel_name}: {e}")
                
    #data Handler
    def write_to_json(self, data, filename):
        # Ensure 'baji_json_folder' exists
        folder_path = "baji_json_folder"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)  # Create the folder if it doesn't exist
            logging.info(f"Created folder: {folder_path}")
        
        # Full file path for saving the JSON file
        full_path = os.path.join(folder_path, filename)
        
        try:
            with open(full_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
                logging.info(f"Data written to {full_path}")
        except Exception as e:
            logging.error(f"Error writing data to JSON file {full_path}: {str(e)}")

    def upload_to_google_sheets(self, data):
        print(data)
        try:
            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
            credentials = Credentials.from_service_account_file(self.service_account_file, scopes=SCOPES)
            service = build('sheets', 'v4', credentials=credentials)

            # Prepare the values to be uploaded to Google Sheets
            values = [["Date", "Post ID", "Link", "Views", "Reactions"]]  # Header row
            
            for post in data:
                # Store each post's data in the database first
                self.store_data(
                    post['Date'],
                    post['Post ID'],
                    post['Link'],
                    post['Views'],
                    post['Reactions']
                )
                # Append the post data to the values list
                values.append(list(post.values()))

            # Prepare the request to update Google Sheets
            request = service.spreadsheets().values().update(
                spreadsheetId=self.sheet_id,
                range='Telegram: Page Insights!A1',
                valueInputOption='RAW',
                body={'values': values}
            )

            # Execute the request
            response = request.execute()
            logging.info(f"Data uploaded to Google Sheets: {response}")
        except Exception as e:
            logging.error(f"Error uploading data to Google Sheets: {str(e)}")
   

    def create_driver(self):
        logging.info("Creating WebDriver instance...")
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--remote-debugging-port=9222")  # Set a specific port

        service = Service(self.driver_path)
        try:
            driver = webdriver.Chrome(service=service, options=chrome_options)
            logging.info("WebDriver created successfully!")
            return driver
        except Exception as e:
            logging.error(f"Failed to create WebDriver: {e}")
            raise


    def click_element(self, xpath):
        try:
            logging.info(f"Trying to click element with XPath: {xpath}...")
            element = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
            logging.info(f"Clicked element with XPath: {xpath}")
        except Exception as e:
            logging.error(f"Error clicking element by XPath {xpath}: {str(e)}")

    def input_text(self, xpath, text):
        try:
            logging.info(f"Trying to input text into element with XPath: {xpath}...")
            input_field = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            input_field.send_keys(text)
            logging.info(f"Entered text into field with XPath: {xpath}")
        except Exception as e:
            logging.error(f"Error entering text into field by XPath {xpath}: {str(e)}")

    #click show more option
    def click_show_more(self, xpath, xpaths_modals, clicks=5, wait_time=5):
        for i in range(clicks):
            try:
                logging.info(f"Attempt {i+1}: Trying to click 'Show More' button with XPath: {xpath}...")
                show_more_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                # Scroll the element into view
                self.driver.execute_script("arguments[0].scrollIntoView(true);", show_more_button)

                self.driver.execute_script("arguments[0].click();", show_more_button)
                logging.info(f"Clicked 'Show More' button {i+1} time(s).")
                time.sleep(wait_time)

                # Check if a modal appears after clicking "Show More" and close it
                # if i == 0:  # Assume the modal appears on the first click of "Show More"
                #     logging.info("Checking for modal to close...")
                #     self.close_modals(xpaths_modals)  # Close the modal using provided XPaths
                if i == 2:
                    print(f"we need to clicked archived...")
                    self.close_modals(xpaths_modals) 
                    time.sleep(10)
                    # # //*[@id="headlessui-dialog-panel-:r6c:"]/div[1]/div[1]/button/i
                    # //*[@id="headlessui-dialog-panel-:r72:"]/div[1]/div[1]/button/i
                    # //*[@id="headlessui-dialog-panel-:r74:"]/div/div[3]/i
            except Exception as e:
                logging.warning(f"Could not find or click the 'Show More' button on attempt {i+1}: {str(e)}")
                break
    
    # close modal
    def close_modals(self, xpaths):
        """Attempts to close both modals using the provided XPaths."""
        try:
            time.sleep(3)
            # First modal close button
            first_close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpaths['first_xbutton_modal']))
            )
            first_close_button.click()
            logging.info("First modal close button clicked.")
            time.sleep(2)  # Wait time before closing the second modal

            # Second modal close button
            second_close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpaths['second_xbutton_modal']))
            )
            second_close_button.click()
            logging.info("Second modal close button clicked.")
            time.sleep(2)  # Ensure everything loads before proceeding to scrape
            return True
        except Exception as e:
            logging.error(f"Failed to close the modals: {str(e)}")
            return False

    def wait_for_manual_login(self, login_confirm_xpath, redirect_url):
        """Waits for manual login, then navigates to the specified URL."""
        logging.info("Waiting for manual login...")
        # print("Please log in to the website manually.")
        try:
            WebDriverWait(self.driver, 300).until(
                EC.presence_of_element_located((By.XPATH, login_confirm_xpath))
            )
            logging.info("Manual login successful. Redirecting to target page...")
            self.driver.get(redirect_url)
            time.sleep(5)
            logging.info(f"Redirected to {redirect_url}")
        except Exception as e:
            logging.error(f"Error waiting for manual login: {str(e)}")
            self.driver.quit()

    def extract_dynamic_post_ids(self):
        logging.info("Starting to extract post data...")
        post_data = []
        max_posts = 500
        base_xpath = "/html/body/main/div[6]/div[2]/div/div/div"

        # Define dynamic paths for post links, dates, views, and reactions
        dynamic_paths = [
            f"{base_xpath}[{{i}}]/div/div[2]/div[1]/a",
            f"{base_xpath}[{{i}}]/div/div[2]/div[2]/a",
            f"{base_xpath}[{{i}}]/div/div[2]/div[3]/a"
        ]

        date_xpaths = [
            f"{base_xpath}[{{i}}]/div/div[6]/div/a",
            f"{base_xpath}[{{i}}]/div/div[7]/div/a",
            f"{base_xpath}[{{i}}]/div/div[8]/div/a",
            f"{base_xpath}[{{i}}]/div/div[9]/div/a",
            f"{base_xpath}[{{i}}]/div/div[10]/div/a"
        ]

        views_xpaths = [
            f"{base_xpath}[{{i}}]/div/div[6]/div/div/p/span[1]",
            f"{base_xpath}[{{i}}]/div/div[7]/div/div/p/span[1]",
            f"{base_xpath}[{{i}}]/div/div[8]/div/div/p/span[1]",
            f"{base_xpath}[{{i}}]/div/div[9]/div/div/p/span[1]",
            f"{base_xpath}[{{i}}]/div/div[10]/div/div/p/span[1]"
        ]

        reaction_xpaths = [
            f"{base_xpath}[{{i}}]/div/div[5]/span",
            f"{base_xpath}[{{i}}]/div/div[5]/span[1]",
            f"{base_xpath}[{{i}}]/div/div[5]/span[2]",
            f"{base_xpath}[{{i}}]/div/div[5]/span[3]",
            f"{base_xpath}[{{i}}]/div/div[5]/span[4]"
        ]

        current_year = datetime.now().year

        for i in range(2, max_posts + 2):
            for path in dynamic_paths:
                try:
                    # Format the path with the current post index
                    post_xpath = path.format(i=i)
                    post_element = self.driver.find_element(By.XPATH, post_xpath)
                    post_id = post_element.get_attribute("href").split('/')[-1]
                    post_link = post_element.get_attribute("href")

                    # Extract dates from multiple XPaths (use the first available date)
                    formatted_date = "Date not available"
                    for date_xpath in date_xpaths:
                        try:
                            date_element = self.driver.find_element(By.XPATH, date_xpath.format(i=i))
                            raw_date = date_element.text.split(',')[0].strip()
                            formatted_date = f"{raw_date}, {current_year}"
                            break  # Break after finding the first valid date
                        except Exception:
                            continue  # Try the next date XPath

                    # Extract views (use the first available view)
                    post_views = "0"
                    for views_xpath in views_xpaths:
                        try:
                            views_element = self.driver.find_element(By.XPATH, views_xpath.format(i=i))
                            post_views = views_element.text
                            break  # Break after finding the first valid view
                        except Exception:
                            continue  # Try the next views XPath

                    # Extract reactions (use the first available unique reaction)
                    unique_reactions = set()  # Use a set to keep unique reactions
                    for reaction_xpath in reaction_xpaths:
                        reaction = self._extract_reaction(reaction_xpath.format(i=i))
                        if reaction != "0":
                            unique_reactions.add(reaction)

                    reactions_string = ", ".join(unique_reactions) if unique_reactions else "0"

                    # Log and print the scraped data
                    logging.info(f"Post {post_id} extracted successfully.")
                    print(f"Scraped Data - Date: {formatted_date}, Post ID: {post_id}, Views: {post_views}, Reactions: {reactions_string}")

                    # Store the extracted data
                    post_data.append({
                        "Date": formatted_date,
                        "Post ID": post_id,
                        "Link": post_link,
                        "Views": post_views,
                        "Reactions": reactions_string
                    })

                    # Optionally store in database
                    self.store_data(formatted_date, post_id, post_link, post_views, reactions_string)

                except Exception as e:
                    logging.debug(f"Error extracting data for post {i}: {str(e)}")
                    continue

        logging.info(f"Extraction completed. Total posts extracted: {len(post_data)}")
        return post_data

    # Store data into database
    def store_data(self, formatted_date, post_id, post_link, post_views, reactions_string):

        """Store data into the MySQL database."""
        insert_query = '''
        INSERT INTO telegram (date, post_id, link, views, reactions) VALUES (%s, %s, %s, %s,%s)
        '''
        try:
            self.cursor.execute(insert_query,(formatted_date ,post_id, post_link, post_views, reactions_string))
            self.conn.commit()
        except Error as e:
            print(f"Error storing data: {e}")

    # extract reaction
    def _extract_reaction(self, xpath):
        try:
            reaction_element = self.driver.find_element(By.XPATH, xpath)
            reaction_text = reaction_element.text.strip()
            return re.findall(r'\d+', reaction_text)[0] if reaction_text else "0"
        except Exception as e:
            logging.debug(f"Reaction not found with XPath {xpath}: {str(e)}")
            return "0"

    # Method to close the browser after completing tasks  
    def close_browser(self):
        print("Closing the browser...")
        self.driver.quit()





