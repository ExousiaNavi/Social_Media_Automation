import logging
import time
import os
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import re
import mysql.connector
from mysql.connector import Error

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class JeetBuzzBot:
    def __init__(self):
        self.driver_path = r'C:\Users\BJ-LAP-65\Downloads\platform\chromedriver-win64\chromedriver.exe'
        self.sheet_id = ''
        self.driver = None
        
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

        self.email = "tech.titan@auroramy.com"
        self.password = "Bernerslee11"
        self.xpaths_common = {
            'sign_in_button': '/html/body/header/nav/div[5]/button',
            'sign_in_with_google': '//*[@id="headlessui-dialog-panel-:r5:"]/div/div[1]/div/button[2]',
            'email_field': '//*[@id="identifierId"]',
            'email_next_button': '//*[@id="identifierNext"]/div/button/span',
            'password_field': '//*[@id="password"]/div[1]/div/div[1]/input',
            'password_next_button': '//*[@id="passwordNext"]/div/button/span',
            'login_confirm': '/html/body/header/nav/div[5]/div'
        }
        self.BRANDS = {
            "JeetBuzz BDT": {
                "url": "https://telemetr.io/en/channels/1737524507-jeetbuzztg",
                "sheet_id": '1lNQiIJp2k_Lmjsu6DoYdvFe50VZuIYE3cF-LIV6FTxA',
                "xpaths": {
                    'show_more_button': "/html/body/main/div[6]/div[1]/div[2]/div/button",
                    'archive_button': "/html/body/main/div[6]/div[1]/div[2]/div/a",
                    'archive_show_more_button': "/html/body/main/div[6]/div[2]/div/button"
                }
            },
            # "JeetBuzz PKR": {
            #     "url": "https://telemetr.io/en/channels/2076805985-jeetbuzz_pkr",
            #     "sheet_id": '1-apCcftt5ChcQG4WOjSebC8WK2OVoJARLWxdKRw8v2Y',
            #     "xpaths": {
            #         'show_more_button': "/html/body/main/div[6]/div[1]/div[2]/div/button",
            #         'archive_button': "/html/body/main/div[6]/div[1]/div[2]/div/a",
            #         'archive_show_more_button': "/html/body/main/div[6]/div[2]/div/button"
            #     }
            # },
            # "JeetBuzz INR": {
            #     "url": "https://telemetr.io/en/channels/1965575618-jeetbuzzinr",
            #     "sheet_id": '1P2qw-amf1ummFgDpXHGn4u5G1gUMySkNW8qjMN7uzAQ',
            #     "xpaths": {
            #         'show_more_button': "/html/body/main/div[6]/div[1]/div[2]/div/button",
            #         'archive_button': "/html/body/main/div[6]/div[1]/div[2]/div/a",
            #         'archive_show_more_button': "/html/body/main/div[6]/div[2]/div/button"
            #     }
            # },
        }
        self.service_account_file = r"C:\Users\BJ-LAP-65\Downloads\platform\performance-424301-244a41249704.json"
        
    def connect_to_db(self):
        """Establish a connection to the MySQL database."""
        try:
            self.conn = mysql.connector.connect(**self.db_config)
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                logging.info("Connected to the database.")
        except Error as e:
            logging.error(f"Error connecting to MySQL: {e}")

    def automate_task(self):
        logging.info("Opening Telegram web...")

        for channel_name, channel_info in self.BRANDS.items():
            self.driver = self.create_driver()
            logging.info(f"Processing {channel_name}...")
            self.sheet_id = channel_info['sheet_id']

            try:
                time.sleep(2)
                self.driver.get("https://telemetr.io/en")
                logging.info("Navigating to the website...")
                time.sleep(3)
                self.click_element(self.xpaths_common['sign_in_button'])
                time.sleep(3)
                self.click_element(self.xpaths_common['sign_in_with_google'])
                time.sleep(5)
                self.input_text(self.xpaths_common['email_field'], self.email)
                time.sleep(3)
                self.click_element(self.xpaths_common['email_next_button'])
                time.sleep(5)
                self.input_text(self.xpaths_common['password_field'], self.password)
                time.sleep(3)
                self.click_element(self.xpaths_common['password_next_button'])
                time.sleep(3)
                self.wait_for_manual_login(self.xpaths_common['login_confirm'], channel_info['url'])
                logging.info("Logged in and redirected to the channel page.")

                xpaths_channel = channel_info['xpaths']
                logging.info("Clicking 'Show More' on the main page...")
                self.click_show_more(xpaths_channel['show_more_button'], clicks=3)
                logging.info("Clicked 'Show More' on the main page.")

                logging.info("Clicking on the Archive button...")
                self.click_element(xpaths_channel['archive_button'])
                logging.info("Clicked on the Archive button.")

                logging.info("Clicking 'Show More' in the Archive page...")
                self.click_show_more(xpaths_channel['archive_show_more_button'], clicks=5)
                logging.info("Clicked 'Show More' in the Archive page.")

                logging.info("Extracting post data...")
                post_data = self.extract_dynamic_post_ids()

                logging.info(f"Extracted post data for {channel_name}:")
                for post in post_data:
                    logging.info(post)

                logging.info(f"Saving data to JSON and uploading to Google Sheets...")
                self.write_to_json(post_data, f'{channel_name}_post_data.json')
                self.upload_to_google_sheets(post_data)

                logging.info(f"Completed processing for {channel_name}\n")
                self.driver.quit()

            except Error as e:
                logging.error()
                
    def write_to_json(self, data, filename):
        folder_path = "baji_json_folder"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)  # Create the folder if it doesn't exist
            logging.info(f"Created folder: {folder_path}")
        
        full_path = os.path.join(folder_path, filename)
        
        try:
            with open(full_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
                logging.info(f"Data written to {full_path}")
        except Exception as e:
            logging.error(f"Error writing data to JSON file {full_path}: {str(e)}")

    def upload_to_google_sheets(self, data):
        try:
            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
            credentials = Credentials.from_service_account_file(self.service_account_file, scopes=SCOPES)
            service = build('sheets', 'v4', credentials=credentials)

            values = [["Date", "Post ID", "Link", "Views", "Reactions"]] + [list(post.values()) for post in data]

            request = service.spreadsheets().values().update(
                spreadsheetId=self.sheet_id,
                range='Telegram: Page Insights!A1',
                valueInputOption='RAW',
                body={'values': values}
            )
            response = request.execute()
            logging.info(f"Data uploaded to Google Sheets: {response}")
        except Exception as e:
            logging.error(f"Error uploading data to Google Sheets: {str(e)}")    

    def create_driver(self):
        logging.info("Creating WebDriver instance...")
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--remote-debugging-port=9222")

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

    def click_show_more(self, xpath, clicks=5, wait_time=5):
        for i in range(clicks):
            try:
                logging.info(f"Attempt {i+1}: Trying to click 'Show More' button with XPath: {xpath}...")
                show_more_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                self.driver.execute_script("arguments[0].click();", show_more_button)
                logging.info(f"Clicked 'Show More' button {i+1} time(s).")
                time.sleep(wait_time)
            except Exception as e:
                logging.error(f"Could not find or click the 'Show More' button on attempt {i+1}: {str(e)}")
                break

    def wait_for_manual_login(self, login_confirm_xpath, redirect_url):
        """Waits for manual login, then navigates to the specified URL."""
        logging.info("Waiting for manual login...")
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
            self.close_browser()

    def extract_dynamic_post_ids(self):
        logging.info("Starting to extract post data...")
        post_data = []
        max_posts = 200
        dynamic_paths = [
            "/html/body/main/div[6]/div[2]/div/div/div[{i}]/div/div[2]/div[1]/a",
            "/html/body/main/div[6]/div[2]/div/div/div[{i}]/div/div[2]/div[2]/a",
            "/html/body/main/div[6]/div[2]/div/div/div[{i}]/div/div[2]/div[3]/a"
        ]
        current_year = datetime.now().year

        for i in range(2, max_posts + 2):
            for path in dynamic_paths:
                try:
                    post_xpath = path.format(i=i)
                    date_xpath = f"/html/body/main/div[6]/div[2]/div/div/div[{i}]/div/div[6]/div/a"
                    views_xpath = f"/html/body/main/div[6]/div[2]/div/div/div[{i}]/div/div[6]/div/div/p/span[1]"
                    reaction_xpaths = [
                        f"/html/body/main/div[6]/div[2]/div/div/div[{i}]/div/div[5]/span[1]",
                        f"/html/body/main/div[6]/div[2]/div/div/div[{i}]/div/div[5]/span[2]",
                        f"/html/body/main/div[6]/div[2]/div/div/div[{i}]/div/div[5]/span[3]",
                    ]
                    logging.info(f"Extracting data for post {i}...")
                    post_element = self.driver.find_element(By.XPATH, post_xpath)
                    date_element = self.driver.find_element(By.XPATH, date_xpath)
                    views_element = self.driver.find_element(By.XPATH, views_xpath)

                    post_id = post_element.get_attribute("href").split('/')[-1]
                    post_link = post_element.get_attribute("href")
                    raw_date = date_element.text.split(',')[0].strip()
                    formatted_date = f"{raw_date}, {current_year}"
                    post_views = views_element.text

                    post_reactions = [self._extract_reaction(reaction_xpath) for reaction_xpath in reaction_xpaths]
                    all_reactions = ", ".join(post_reactions) if post_reactions else "0"


                    post_data.append({
                        "Date": formatted_date,
                        "Post ID": post_id,
                        "Link": post_link,
                        "Views": post_views,
                        "Reactions": all_reactions
                    })

                    logging.info(raw_date)
                    logging.info(f"Post {post_id} extracted successfully.")
                    self.store_data(formatted_date, post_id, post_link, post_views, all_reactions)

                except Exception as e:
                    logging.error(f"Error extracting data for post {i}: {str(e)}")
                    continue
        logging.info(f"Extraction completed. Total posts extracted: {len(post_data)}")
        return post_data
    
    def store_data(self, formatted_date, post_id, post_link, post_views, all_reactions):
        """Store data into the MySQL database."""
        insert_query = '''
        INSERT INTO telegram (date, post_id, link, views, reactions) VALUES (%s, %s, %s, %s,%s)
        '''
        try:
            self.cursor.execute(insert_query, (formatted_date, post_id, post_link, post_views, all_reactions))
            self.conn.commit()
            logging.info(f"Data for post {post_id} stored successfully.")
        except Error as e:
            logging.error(f"Error storing data: {e}")

    def _extract_reaction(self, xpath):
        try:
            reaction_element = self.driver.find_element(By.XPATH, xpath)
            reaction_text = reaction_element.text.strip()
            return re.findall(r'\d+', reaction_text)[0] if reaction_text else "0"
        except Exception as e:
            logging.error(f"Reaction not found with XPath {xpath}: {str(e)}")
            return "0"

    def close_browser(self):
        logging.info("Closing the browser...")
        if self.driver:
            self.driver.quit()

# Example usage
if __name__ == "__main__":
    bot = JeetBuzzBot()
    bot.automate_task()
