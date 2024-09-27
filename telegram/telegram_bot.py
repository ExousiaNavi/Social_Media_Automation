# import logging
# import time
# # from scraper import WebScraper
# # from data_handler import DataHandler
# # from config import BRANDS
# import os
# import json
# from google.oauth2.service_account import Credentials
# from googleapiclient.discovery import build
# from selenium import webdriver
# from utilities.browser import Browser
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from datetime import datetime
# import re
# from selenium.webdriver.chrome.service import Service
# import mysql.connector
# from mysql.connector import Error


# # This class contains the Selenium actions to automate Telegram Web
# class TelegramBot:
#     def __init__(self):
#          # Get the Selenium WebDriver instance from the Browser class
#         self.driver_path = r'C:\Users\BJ-LAP-65\Documents\GitHub\Social_Media_Automation\chromedriver-win64\chromedriver.exe'
#         # self.channel_url = ''
#         self.sheet_id = ''
#         self.driver = ''
#         # self.driver = Browser().get_driver()

#         # MySQL Database configuration
#         self.db_config = {
#                 'host': 'localhost', # Replace with your MySQL host
#                 'user': 'root',  # Replace with your MySQL username
#                 'password': '',  # Replace with your MySQL password
#                 'database': 'datasource'  # Replace with your MySQL database
#             }

#         self.conn = None
#         self.cursor = None
#         self.connect_to_db()

#     def connect_to_db(self):
#                 """Establish a connection to the MySQL database."""
#                 try:
#                     self.conn = mysql.connector.connect(**self.db_config)
#                     if self.conn.is_connected():
#                         self.cursor = self.conn.cursor()
#                         # self.create_table()
#                         print("Connected to the database.")
#                 except Error as e:
#                     print(f"Error connecting to MySQL: {e}")

#                 self.email = "paulabutar7@gmail.com"
#                 self.password = "Bernerslee11"
#                 self.xpaths_common = {
#                 'sign_in_button': '/html/body/header/nav/div[5]/button',
#                 'sign_in_with_google': '//*[@id="headlessui-dialog-panel-:r5:"]/div/div[1]/div/button[2]',
#                 'email_field': '//*[@id="identifierId"]',
#                 'email_next_button': '//*[@id="identifierNext"]/div/button/span',
#                 'password_field': '//*[@id="password"]/div[1]/div/div[1]/input',
#                 'password_next_button': '//*[@id="passwordNext"]/div/button/span',
#                 'login_confirm': '/html/body/header/nav/div[5]'
#             }   
#                 self.BRANDS = {
#                     # Commented out BDT, INR, and NPR for testing PKR
#                     "Baji BDT": {
#                         "url": "https://telemetr.io/en/channels/1829680439-baji_bgd/publish",
#                         "sheet_id": '1V1aVnO_ShcEh5ZQG37DfYijdeS3rLkeyRb8Fn-xHeWk',
#                         "xpaths": {
#                             'show_more_button': "/html/body/main/div[6]/div[2]/div[2]/div[2]/div/button",
#                             'archive_button': "/html/body/main/div[6]/div[2]/div[2]/div[2]/div/a",
#                             'archive_show_more_button': "/html/body/main/div[6]/div[2]/div/button"
#                         }
#                     },
#                     "Baji INR": {
#                         "url": "https://telemetr.io/en/channels/1545322793-baji_ind",
#                         "sheet_id": '1MTfTxWFgvmlYbGIGH9NjGsH7WfExOZqEbqdPlUDsjkU',
#                         "xpaths": {
#                             'show_more_button': "/html/body/main/div[6]/div[1]/div[2]/div/button",
#                             'archive_button': "/html/body/main/div[6]/div[1]/div[2]/div/a",
#                             'archive_show_more_button': "/html/body/main/div[6]/div[2]/div/button"
#                         }
#                     },
#                     "BAJI PKR": {
#                         "url": "https://telemetr.io/en/channels/1803180364-baji_pak",
#                         "sheet_id": '15CzG1X34AwKOysHvO4Nb1NRG3tdUFzEVU3QnFu_Hvdw',
#                         "xpaths": {
#                             'show_more_button': "/html/body/main/div[6]/div[1]/div[2]/div/button",
#                             'archive_button': "/html/body/main/div[6]/div[1]/div[2]/div/a",
#                             'archive_show_more_button': "/html/body/main/div[6]/div[2]/div/button"
#                         }
#                     },
#                     "BAJI NPR": {
#                         "url": "https://telemetr.io/en/channels/2058296847-baji_npl",
#                         "sheet_id": '16QpRAQesYTK85zmLU4L1nEusfhXVySPuq4DihCrSsYs',
#                         "xpaths": {
#                             'show_more_button': "/html/body/main/div[6]/div[1]/div[2]/div/button",
#                             'archive_button': "/html/body/main/div[6]/div[1]/div[2]/div/a",
#                             'archive_show_more_button': "/html/body/main/div[6]/div[2]/div/button"
#                         }
#                     }
#                 }

#                 self.service_account_file = r"C:\Users\BJ-LAP-65\Documents\GitHub\Social_Media_Automation\all-brands-performance-3711739d3e51.json"

#     # Method to open Telegram Web using Selenium
#     def automate_task(self, max_retries=3, retry_delay=5):
#             print("Opening Telegram web...")
#         # Navigate to Telegram Web
#         # self.driver.get("https://web.telegram.org")
#             try:
#                 for channel_name, channel_info in self.BRANDS.items():
#                     # Create a driver
#                     self.driver = self.create_driver()
#                     logging.info(f"Processing {channel_name}...")
#                     self.sheet_id = channel_info['sheet_id']

#                     # If no cookies or expired session, log in manually
#                     time.sleep(3)
#                     self.driver.get("https://telemetr.io/en")
#                     print("Navigating to the website...")
#                     # Click the elements to login
#                     self.click_element(self.xpaths_common['sign_in_button'])
#                     time.sleep(3)
#                     self.click_element(self.xpaths_common['sign_in_with_google'])
#                     # Input email and password
#                     time.sleep(3)
#                     self.input_text(self.xpaths_common['email_field'], self.email)
#                     time.sleep(3)
#                     self.click_element(self.xpaths_common['email_next_button'])
#                     time.sleep(5)
#                     self.input_text(self.xpaths_common['password_field'], self.password)
#                     time.sleep(5)
#                     self.click_element(self.xpaths_common['password_next_button'])
#                     time.sleep(5)
#                     # Wait for manual login
#                     self.wait_for_manual_login(self.xpaths_common['login_confirm'], channel_info['url'])
#                     # Save cookies after successful login
                
#                     # Continue with the rest of your scraping process
#                     xpaths_channel = channel_info['xpaths']
                        
#                     # Use the correct modal XPaths based on the brand
#                     # xpaths_modals = {
#                     #     "first_xbutton_modal": "/html/body/main/div[6]/div[2]/div/div/div[2]/div[2]/button",  # Example XPath
#                     #     "second_xbutton_modal": "/html/body/main/div[6]/div[2]/div/div/div[2]/div[3]/i"       # Example XPath
#                     # }
#                     # //*[@id="headlessui-dialog-panel-:r72:"]/div[1]/div[1]/button/i
#                     #     //*[@id="headlessui-dialog-panel-:r74:"]/div/div[3]/i
#                     xpaths_modals = {
#                         "first_xbutton_modal": "//*[starts-with(@id, 'headlessui-dialog-panel')]/div[1]/div[1]/button",  # Example XPath
#                         "second_xbutton_modal": "//*[starts-with(@id, 'headlessui-dialog-panel')]/div/div[3]/i"       # Example XPath
#                     }
                        
#                     # Click "Show More" and close modals if they appear
#                     self.click_show_more(xpaths_channel['show_more_button'], xpaths_modals, clicks=3)
#                     print("Clicked 'Show More' on the main page...")
                    
#                     self.click_element(xpaths_channel['archive_button'])
#                     print("Clicked on the Archive button...")

#                     self.click_show_more(xpaths_channel['archive_show_more_button'], xpaths_modals, clicks=5)
#                     print("Clicked 'Show More' in the Archive page...")

            
#                     post_data = self.extract_dynamic_post_ids()

#                     # Print the extracted post data for visibility
#                     print(f"Extracted post data for {channel_name}:")
#                     # for post in post_data:
#                     #     print(post) 
#                     self.write_to_json(post_data, f'{channel_name}_post_data.json')
#                     # self.upload_to_google_sheets(post_data)

#                     logging.info(f"Completed processing for {channel_name}\n")
#                     self.driver.quit()

#             except Exception as e:
#                     logging.error(f"Error processing automation task {channel_name}: {e}")
                
#     #data Handler
#     def write_to_json(self, data, filename):
#         # Ensure 'baji_json_folder' exists
#         folder_path = "baji_json_folder"
#         if not os.path.exists(folder_path):
#             os.makedirs(folder_path)  # Create the folder if it doesn't exist
#             logging.info(f"Created folder: {folder_path}")
        
#         # Full file path for saving the JSON file
#         full_path = os.path.join(folder_path, filename)
        
#         try:
#             with open(full_path, 'w', encoding='utf-8') as file:
#                 json.dump(data, file, indent=4)
#                 logging.info(f"Data written to {full_path}")
#         except Exception as e:
#             logging.error(f"Error writing data to JSON file {full_path}: {str(e)}")

#     def upload_to_google_sheets(self, data):
#         print(data)
#         try:
#             SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#             credentials = Credentials.from_service_account_file(self.service_account_file, scopes=SCOPES)
#             service = build('sheets', 'v4', credentials=credentials)

#             # Prepare the values to be uploaded to Google Sheets
#             values = [["Date", "Post ID", "Link", "Views", "Reactions"]]  # Header row
            
#             for post in data:
#                 # Store each post's data in the database first
#                 self.store_data(
#                     post['Date'],
#                     post['Post ID'],
#                     post['Link'],
#                     post['Views'],
#                     post['Reactions']
#                 )
#                 # Append the post data to the values list
#                 values.append(list(post.values()))

#             # Prepare the request to update Google Sheets
#             request = service.spreadsheets().values().update(
#                 spreadsheetId=self.sheet_id,
#                 range='Telegram: Page Insights!A1',
#                 valueInputOption='RAW',
#                 body={'values': values}
#             )

#             # Execute the request
#             response = request.execute()
#             logging.info(f"Data uploaded to Google Sheets: {response}")
#         except Exception as e:
#             logging.error(f"Error uploading data to Google Sheets: {str(e)}")
   

#     def create_driver(self):
#         logging.info("Creating WebDriver instance...")
#         chrome_options = Options()
#         chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#         chrome_options.add_argument("--incognito")
#         chrome_options.add_argument("--remote-debugging-port=9222")  # Set a specific port

#         service = Service(self.driver_path)
#         try:
#             driver = webdriver.Chrome(service=service, options=chrome_options)
#             logging.info("WebDriver created successfully!")
#             return driver
#         except Exception as e:
#             logging.error(f"Failed to create WebDriver: {e}")
#             raise


#     def click_element(self, xpath):
#         try:
#             logging.info(f"Trying to click element with XPath: {xpath}...")
#             element = WebDriverWait(self.driver, 60).until(
#                 EC.element_to_be_clickable((By.XPATH, xpath))
#             )
#             element.click()
#             logging.info(f"Clicked element with XPath: {xpath}")
#         except Exception as e:
#             logging.error(f"Error clicking element by XPath {xpath}: {str(e)}")

#     def input_text(self, xpath, text):
#         try:
#             logging.info(f"Trying to input text into element with XPath: {xpath}...")
#             input_field = WebDriverWait(self.driver, 30).until(
#                 EC.presence_of_element_located((By.XPATH, xpath))
#             )
#             input_field.send_keys(text)
#             logging.info(f"Entered text into field with XPath: {xpath}")
#         except Exception as e:
#             logging.error(f"Error entering text into field by XPath {xpath}: {str(e)}")

#     #click show more option
#     def click_show_more(self, xpath, xpaths_modals, clicks=5, wait_time=5):
#         for i in range(clicks):
#             try:
#                 logging.info(f"Attempt {i+1}: Trying to click 'Show More' button with XPath: {xpath}...")
#                 show_more_button = WebDriverWait(self.driver, 10).until(
#                     EC.presence_of_element_located((By.XPATH, xpath))
#                 )
#                 # Scroll the element into view
#                 self.driver.execute_script("arguments[0].scrollIntoView(true);", show_more_button)

#                 self.driver.execute_script("arguments[0].click();", show_more_button)
#                 logging.info(f"Clicked 'Show More' button {i+1} time(s).")
#                 time.sleep(wait_time)

#                 # Check if a modal appears after clicking "Show More" and close it
#                 # if i == 0:  # Assume the modal appears on the first click of "Show More"
#                 #     logging.info("Checking for modal to close...")
#                 #     self.close_modals(xpaths_modals)  # Close the modal using provided XPaths
#                 if i == 2:
#                     print(f"we need to clicked archived...")
#                     self.close_modals(xpaths_modals) 
#                     time.sleep(10)
#                     # # //*[@id="headlessui-dialog-panel-:r6c:"]/div[1]/div[1]/button/i
#                     # //*[@id="headlessui-dialog-panel-:r72:"]/div[1]/div[1]/button/i
#                     # //*[@id="headlessui-dialog-panel-:r74:"]/div/div[3]/i
#             except Exception as e:
#                 logging.warning(f"Could not find or click the 'Show More' button on attempt {i+1}: {str(e)}")
#                 break
    
#     # close modal
#     def close_modals(self, xpaths):
#         """Attempts to close both modals using the provided XPaths."""
#         try:
#             time.sleep(3)
#             # First modal close button
#             first_close_button = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, xpaths['first_xbutton_modal']))
#             )
#             first_close_button.click()
#             logging.info("First modal close button clicked.")
#             time.sleep(2)  # Wait time before closing the second modal

#             # Second modal close button
#             second_close_button = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, xpaths['second_xbutton_modal']))
#             )
#             second_close_button.click()
#             logging.info("Second modal close button clicked.")
#             time.sleep(2)  # Ensure everything loads before proceeding to scrape
#             return True
#         except Exception as e:
#             logging.error(f"Failed to close the modals: {str(e)}")
#             return False

#     def wait_for_manual_login(self, login_confirm_xpath, redirect_url):
#         """Waits for manual login, then navigates to the specified URL."""
#         logging.info("Waiting for manual login...")
#         # print("Please log in to the website manually.")
#         try:
#             WebDriverWait(self.driver, 300).until(
#                 EC.presence_of_element_located((By.XPATH, login_confirm_xpath))
#             )
#             logging.info("Manual login successful. Redirecting to target page...")
#             self.driver.get(redirect_url)
#             time.sleep(5)
#             logging.info(f"Redirected to {redirect_url}")
#         except Exception as e:
#             logging.error(f"Error waiting for manual login: {str(e)}")
#             self.driver.quit()

#     def extract_dynamic_post_ids(self):
#         logging.info("Starting to extract post data...")
#         post_data = []
#         max_posts = 1000
#         base_xpath = "/html/body/main/div[6]/div[2]/div/div/div"

#         # Define dynamic paths for post links, dates, views, and reactions
#         dynamic_paths = [
#             f"{base_xpath}[{{i}}]/div/div[2]/div[1]/a",
#             f"{base_xpath}[{{i}}]/div/div[2]/div[2]/a",
#             f"{base_xpath}[{{i}}]/div/div[2]/div[3]/a"
#         ]

#         date_xpaths = [
#             f"{base_xpath}[{{i}}]/div/div[6]/div/a",
#             f"{base_xpath}[{{i}}]/div/div[7]/div/a",
#             f"{base_xpath}[{{i}}]/div/div[8]/div/a",
#             f"{base_xpath}[{{i}}]/div/div[9]/div/a",
#             f"{base_xpath}[{{i}}]/div/div[10]/div/a"
#         ]

#         views_xpaths = [
#             f"{base_xpath}[{{i}}]/div/div[6]/div/div/p/span[1]",
#             f"{base_xpath}[{{i}}]/div/div[7]/div/div/p/span[1]",
#             f"{base_xpath}[{{i}}]/div/div[8]/div/div/p/span[1]",
#             f"{base_xpath}[{{i}}]/div/div[9]/div/div/p/span[1]",
#             f"{base_xpath}[{{i}}]/div/div[10]/div/div/p/span[1]"
#         ]

#         reaction_xpaths = [
#             f"{base_xpath}[{{i}}]/div/div[5]/span",
#             f"{base_xpath}[{{i}}]/div/div[5]/span[1]",
#             f"{base_xpath}[{{i}}]/div/div[5]/span[2]",
#             f"{base_xpath}[{{i}}]/div/div[5]/span[3]",
#             f"{base_xpath}[{{i}}]/div/div[5]/span[4]"
#         ]

#         current_year = datetime.now().year

#         for i in range(2, max_posts + 2):
#             for path in dynamic_paths:
#                 try:
#                     # Format the path with the current post index
#                     post_xpath = path.format(i=i)
#                     post_element = self.driver.find_element(By.XPATH, post_xpath)
#                     post_id = post_element.get_attribute("href").split('/')[-1]
#                     post_link = post_element.get_attribute("href")

#                     # Extract dates from multiple XPaths (use the first available date)
#                     formatted_date = "Date not available"
#                     for date_xpath in date_xpaths:
#                         try:
#                             date_element = self.driver.find_element(By.XPATH, date_xpath.format(i=i))
#                             raw_date = date_element.text.split(',')[0].strip()
#                             formatted_date = f"{raw_date}, {current_year}"
#                             break  # Break after finding the first valid date
#                         except Exception:
#                             continue  # Try the next date XPath

#                     # Extract views (use the first available view)
#                     post_views = "0"
#                     for views_xpath in views_xpaths:
#                         try:
#                             views_element = self.driver.find_element(By.XPATH, views_xpath.format(i=i))
#                             post_views = views_element.text
#                             break  # Break after finding the first valid view
#                         except Exception:
#                             continue  # Try the next views XPath

#                     # Extract reactions (use the first available unique reaction)
#                     unique_reactions = set()  # Use a set to keep unique reactions
#                     for reaction_xpath in reaction_xpaths:
#                         reaction = self._extract_reaction(reaction_xpath.format(i=i))
#                         if reaction != "0":
#                             unique_reactions.add(reaction)

#                     reactions_string = ", ".join(unique_reactions) if unique_reactions else "0"

#                     # Log and print the scraped data
#                     logging.info(f"Post {post_id} extracted successfully.")
#                     print(f"Scraped Data - Date: {formatted_date}, Post ID: {post_id}, Views: {post_views}, Reactions: {reactions_string}")

#                     # Store the extracted data
#                     post_data.append({
#                         "Date": formatted_date,
#                         "Post ID": post_id,
#                         "Link": post_link,
#                         "Views": post_views,
#                         "Reactions": reactions_string
#                     })

#                     # Optionally store in database
#                     self.store_data(formatted_date, post_id, post_link, post_views, reactions_string)

#                 except Exception as e:
#                     logging.debug(f"Error extracting data for post {i}: {str(e)}")
#                     continue

#         logging.info(f"Extraction completed. Total posts extracted: {len(post_data)}")
#         return post_data

#     # Store data into database
#     def store_data(self, formatted_date, post_id, post_link, post_views, reactions_string):

#         """Store data into the MySQL database."""
#         insert_query = '''
#         INSERT INTO telegram (date, post_id, link, views, reactions) VALUES (%s, %s, %s, %s,%s)
#         '''
#         try:
#             self.cursor.execute(insert_query,(formatted_date ,post_id, post_link, post_views, reactions_string))
#             self.conn.commit()
#         except Error as e:
#             print(f"Error storing data: {e}")

#     # extract reaction
#     def _extract_reaction(self, xpath):
#         try:
#             reaction_element = self.driver.find_element(By.XPATH, xpath)
#             reaction_text = reaction_element.text.strip()
#             return re.findall(r'\d+', reaction_text)[0] if reaction_text else "0"
#         except Exception as e:
#             logging.debug(f"Reaction not found with XPath {xpath}: {str(e)}")
#             return "0"

#     # Method to close the browser after completing tasks  
#     def close_browser(self):
#         print("Closing the browser...")
#         self.driver.quit()






import asyncio
import logging
import os
import json
import re
import urllib.parse
import requests
from datetime import datetime
from fake_useragent import UserAgent, FakeUserAgentError
from playwright.async_api import async_playwright
import mysql.connector
from mysql.connector import Error

class TelegramBot:
    MAX_RETRIES = 5  # Maximum number of retries in case of error
    RETRY_DELAY = 5  # Delay between retries (in seconds)
    logging.basicConfig(level=logging.INFO)
    def __init__(self):
        # Playwright browser setup
        self.sheet_id = ''
        self.page = None
        
        # MySQL Database configuration
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'datasource'
        }
        
        self.conn = None
        self.cursor = None
        self.connect_to_db()
        self.cookies = None
        self.email = "paulabutar7@gmail.com"
        self.password = "Bernerslee11"
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

    def connect_to_db(self):
        """Establish a connection to the MySQL database."""
        try:
            self.conn = mysql.connector.connect(**self.db_config)
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print("Connected to the database.")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    
    async def run(self, email, password, main_url, currency, url):
        """Main wrapper to handle retries."""
        retries = 0
        while retries < self.MAX_RETRIES:
            try:
                await self.automate_task(email, password, main_url, currency, url)
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

    async def automate_task(self, email, password, main_url, currency, url):
        """Main method to run Playwright automation."""
        async with async_playwright() as p:
            # Using fake-useragent to generate a random user agent for each session
            try:
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

            # Perform login
            try:
                await self.page.locator(self.xpaths_common['sign_in_button']).nth(0).click()
                await self.page.click(self.xpaths_common['sign_in_with_google'])
                await self.page.fill(self.xpaths_common['email_field'], email)
                await self.page.click(self.xpaths_common['email_next_button'])
                await self.page.fill(self.xpaths_common['password_field'], password)
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
            await self.page.goto(url)
            logging.info(f"Navigated to {url}")
            await asyncio.sleep(10)
            # await self.page.locator(self.xpaths_common['just_browse']).click(force=True)
            await self.page.locator(self.xpaths_common['accept_all']).click(force=True)
            # Click "Show More"
            await self.click_show_more(self.xpaths_common['show_more_button'], 3, 'out', currency)
                
            await self.page.click(self.xpaths_common['archive_button'])
               
            
            await asyncio.sleep(2)
            await self.click_show_more(self.xpaths_common['archive_show_more_button'], 5, 'in', currency)
                
                
                

            # Extract posts data
            # post_data = await self.extract_dynamic_post_ids()

            # Write data to JSON
            # self.write_to_json(post_data, f'{channel_name}_post_data.json')

            await browser.close()
            
    # Function to remove unwanted fields from each message
    async def filter_response(self, data, fields):
        filtered_messages = []
        for message in data['messages']:
            filtered_message = {k: v for k, v in message.items() if k not in fields}
            filtered_messages.append(filtered_message)
        return {"messages": filtered_messages}


    async def sendApiRequest(self, cursor, currency):
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

                    logging.info(f"Response: {response.status_code}, {cursor_value}")
                    # Define the fields you want to remove
                    fields_to_remove = ['channel', 'message', 'mediaRaw', 'entities', 'album', 'photo', 'video', 'isAd','emoticon','deletedAt','forwardsCount']
                    # Filter the response
                    filtered_response = await self.filter_response(response.json(), fields_to_remove)

                    channel_name = currency+'_'+cursor_value
                    self.write_to_json(filtered_response, f'{channel_name}_post_data.json')
                        
                        
                            
    async def click_show_more(self, show_more_xpath, clicks, t, currency):
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
                        await self.sendApiRequest(href, currency)
                    else:
                        print("No href found for this button.")
                await show_more_button.click(force=True)
                logging.info(f"Clicked 'Show More' {i+1} time(s).")
                await self.page.wait_for_timeout(2000)  # Wait 5 seconds between clicks
            except Exception as e:
                logging.error(f"Error clicking 'Show More': {e}")
                break

    # async def extract_dynamic_post_ids(self):
    #     """Extract dynamic post data."""
    #     post_data = []
    #     max_posts = 1000
    #     logging.info(f"Proceed to api now...")
    #     url = 'https://gw-prod.telemetr.io/store.v1.Messages/ChannelMessages'
    #     payload = {
    #         "channel": {"telegramId": "1829680439"},
    #         "returnShortInfo": True,
    #         "cursor": "CLIM"
    #     }

    #     headers = {
    #         'Accept': 'application/json',
    #         'Content-Type': 'application/json'
    #     }

    #     response = requests.post(url, json=payload, headers=headers)
    #     logging.info(f"Response: {response.status_code}, {response.text}")
    #     # print(response.json())
    #     # for i in range(2, max_posts + 2):
    #     #     try:
    #     #         # Check if the post link exists before trying to get the attribute
    #     #         post_link_element = self.page.locator(f'//div[@data-post-id="{i}"]/a')
    #     #         if await post_link_element.count() == 0:
    #     #             logging.info(f"Post link not found for post {i}, skipping...")
    #     #             continue  # Skip this iteration if the post link is not found

    #     #         # If the element exists, get the 'href' attribute
    #     #         post_link = await post_link_element.get_attribute('href', timeout=10000)
    #     #         post_id = post_link.split('/')[-1]

    #     #         # Extract other information only if the post_link is found
    #     #         date = await self.page.inner_text(f'//div[@data-post-id="{i}"]//time', timeout=10000)
    #     #         views = await self.page.inner_text(f'//div[@data-post-id="{i}"]//span[@class="views"]', timeout=10000)
    #     #         reactions = await self.page.inner_text(f'//div[@data-post-id="{i}"]//span[@class="reactions"]', timeout=10000)

    #     #         # Append the extracted data to post_data
    #     #         post_data.append({
    #     #             "Date": date,
    #     #             "Post ID": post_id,
    #     #             "Link": post_link,
    #     #             "Views": views,
    #     #             "Reactions": reactions
    #     #         })

    #     #         logging.info(f"Iteration count: {i}")
            
    #     #     except Exception as e:
    #     #         logging.error(f"Error extracting post {i}: {e}")



    #     # return post_data

    def write_to_json(self, data, filename):
        folder_path = "baji_json_folder"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        full_path = os.path.join(folder_path, filename)
        try:
            with open(full_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
                logging.info(f"Data written to {full_path}")
        except Exception as e:
            logging.error(f"Error writing data to JSON file {full_path}: {e}")
# # To run the bot
# if __name__ == "__main__":
#     bot = TelegramBotPlaywright()
#     asyncio.run(bot.automate_task())
