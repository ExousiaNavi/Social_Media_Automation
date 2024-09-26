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
import csv
import concurrent.futures
from tqdm import tqdm  # Progress bar library
from google.oauth2 import service_account
import mysql.connector
from mysql.connector import Error

# This class contains the Selenium actions to automate Twitter Web
class WinrsPKRTwitterBot:
    def __init__(self):
        self.driver = Browser().get_driver()
        # Define constants
        self.SERVICE_ACCOUNT_FILE = r'C:\Users\BJ-LAP-65\Downloads\platform\performance-424301-244a41249704.json'
        # Authenticate and build the service
        self.credentials = service_account.Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
        self.service = build('sheets', 'v4', credentials=self.credentials)
        # List of dictionaries containing the configurations for each sheet
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

        self.sheets_config = [
            {
                "source_spreadsheet_id": '1WJJzL3WGUkdCnCv3KQxEePOx682PHY1D8rVgfV8Yv4g',
                "source_range_name": 'Twitter!K1:K1000',
                "target_spreadsheet_id": '1_UC_C6a_Z10yxrQaXCJjtxx_D47p_UQ7JK44TUg5-sI',
                "target_range_name": 'WinRS PKR !A2',  # Start data from row 2 (after headers)
                "sheet_label": 'WinRS PKR  Sheet',
                "target_sheet_name": 'WinRS PKR '
            },
        ]
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

   
    def store_data(self, date_formatted, url, views_text, likes_text ):
        """Store data into the MySQL database."""
        insert_query = '''
        INSERT INTO twitter (date, url, views, likes) VALUES (%s, %s, %s, %s)
        '''
        try:
            self.cursor.execute(insert_query,(date_formatted,url, views_text, likes_text))
            self.conn.commit()
        except Error as e:
            print(f"Error storing data: {e}")


    def get_hyperlinks(self, spreadsheet_id, range_name):
        """Fetches the hyperlinks from the Google Sheet."""
        try:
            sheet = self.service.spreadsheets().get(
                spreadsheetId=spreadsheet_id, ranges=range_name, includeGridData=True
            ).execute()
            data = sheet['sheets'][0]['data'][0]['rowData']
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

        urls = []
        for row in data:
            for cell in row.get('values', []):
                if 'hyperlink' in cell.get('effectiveValue', {}):
                    urls.append(cell['effectiveValue']['hyperlink'])
                elif 'userEnteredFormat' in cell and 'textFormat' in cell['userEnteredFormat']:
                    text_format = cell['userEnteredFormat']['textFormat']
                    if 'link' in text_format and 'uri' in text_format['link']:
                        urls.append(text_format['link']['uri'])
        return urls
    def create_driver(self):
        """Create a new instance of the Chrome driver (non-headless mode to allow viewing)."""
        options = webdriver.ChromeOptions()
        # options.add_argument('--disable-gpu')
        # options.add_argument('--no-sandbox')
        options.add_argument('--headless')  # Headless mode
        driver = webdriver.Chrome(options=options)

        return driver
    
    def extract_data(self, url):
        """Extracts data from the given URL and returns it in a structured format."""
        driver = self.create_driver()  # Create a new driver for each URL
        driver.get(url)
        
        # Wait until the page is fully loaded by checking the document readiness
        WebDriverWait(driver, 30).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

        # Ensure additional time for slow-loading elements (adjustable if necessary)
        time.sleep(2)

        def get_text_by_xpath(xpath, alt_xpath=None):
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                return element.text if element.text else "0"
            except Exception:
                if alt_xpath:
                    return get_text_by_xpath(alt_xpath)
                return "0"

        try:
            # Extract Date from the tweet
            try:
                datetime_element = driver.execute_script(
                    "return document.querySelector('time')?.getAttribute('datetime');"
                )
                if datetime_element:
                    datetime_obj = datetime.fromisoformat(datetime_element.replace('Z', '+00:00'))
                    date_formatted = datetime_obj.strftime('%Y-%m-%d')  # Extract only date (YYYY-MM-DD)
                else:
                    date_formatted = "No value"
            except Exception as e:
                print(f"Error extracting date: {e}")
                date_formatted = "No value"

            # Extract Views using the provided XPath
            views_text = get_text_by_xpath(
                '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[4]/div/div[1]/div/div[3]/span/div/span/span/span'
            )

            # Extract Likes with the fallback XPath
            likes_text = get_text_by_xpath(
                '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div[4]/a/div/span/span/span',
                '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div[2]/a/div/span/span/span'
            )

            self.store_data(date_formatted, url, views_text, likes_text)
            return {"Date": date_formatted, "URL": url, "Views": views_text, "Likes": likes_text}  # Return JSON structure
        
        except Exception as e:
            print(f"An error occurred while extracting data from {url}: {e}")
            return {"Date": "Error", "URL": url, "Views": "Error", "Likes": "Error"}
        
        finally:
            driver.quit()  # Ensure the driver is closed after each URL

    def clear_columns(self,spreadsheet_id, sheet_name):
        """Clears the entire columns A to D in the specified Google Sheet."""
        clear_range = f"{sheet_name}!A:D"  # Clear columns A to D
        try:
            self.service.spreadsheets().values().clear(spreadsheetId=spreadsheet_id, range=clear_range).execute()
            print(f"Cleared columns A to D in sheet {sheet_name}.")
        except Exception as e:
            print(f"An error occurred while clearing columns: {e}")

    def append_to_sheet(self, spreadsheet_id, range_name, values, retries=3):
        """Appends the extracted data to the specified Google Sheet with retries."""
        body = {
            'values': values
        }
        attempt = 0
        while attempt < retries:
            try:
                result = self.service.spreadsheets().values().append(
                    spreadsheetId=spreadsheet_id,
                    range=range_name,
                    valueInputOption='RAW',
                    insertDataOption='INSERT_ROWS',  # This will append the data
                    body=body
                ).execute()
                print(f"{result.get('updates').get('updatedCells')} cells appended in range {range_name}.")
                break  # Exit loop on success
            except Exception as e:
                print(f"An error occurred while appending to the sheet: {e}")
                attempt += 1
                time.sleep(2)  # Add a small delay before retrying
    
    def add_headers(self,spreadsheet_id, sheet_name):
        """Adds headers (Date, URL, Views, Likes) to the Google Sheet in row 1."""
        headers = [['Date', 'URL', 'Views', 'Likes']]
        body = {
            'values': headers
        }
        try:
            result = self.service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id,
                range=f"{sheet_name}!A1:D1",  # Adding headers to row 1
                valueInputOption='RAW',
                body=body
            ).execute()
            print(f"Headers added to sheet {sheet_name}.")
        except Exception as e:
            print(f"An error occurred while adding headers: {e}")

    def process_sheet_parallel(self, source_spreadsheet_id, source_range_name, target_spreadsheet_id, target_range_name, sheet_label, target_sheet_name):
        """Processes a single sheet, clears columns, extracts data, adds headers, and writes it back to the Google Sheet."""
        print(f"Processing {sheet_label}...")

        # Clear columns A to D in the target sheet
        self.clear_columns(target_spreadsheet_id, target_sheet_name)

        # Add headers to the target sheet
        self.add_headers(target_spreadsheet_id, target_sheet_name)

        # Fetch URLs from the source Google Sheet
        urls = self.get_hyperlinks(source_spreadsheet_id, source_range_name)
        print("Extracted URLs:")

        # Store the results for JSON output
        results = []

        # Use ThreadPoolExecutor to scrape in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(self.extract_data, url) for url in urls]
            for future in tqdm(concurrent.futures.as_completed(futures), desc=f"Processing URLs for {sheet_label}", total=len(urls)):
                data = future.result()
                results.append(data)  # Collect data for JSON output
                self.append_to_sheet(target_spreadsheet_id, target_range_name, [[data["Date"], data["URL"], data["Views"], data["Likes"]]])

        # Print the final result in JSON format
        # print(f"\nJSON Output for {sheet_label}:")
        # print(json.dumps(results, indent=4))

        print(results)

    # Method to automate Twitter task
    def automate_task(self):
        # Process BDT, INR, NPR, and PKR sheets
        # Loop through each sheet configuration and call the process_sheet_parallel method
        for sheet in self.sheets_config:
            print(sheet['source_spreadsheet_id'])
            self.process_sheet_parallel(
                source_spreadsheet_id=sheet['source_spreadsheet_id'],
                source_range_name=sheet['source_range_name'],
                target_spreadsheet_id=sheet['target_spreadsheet_id'],
                target_range_name=sheet['target_range_name'],
                sheet_label=sheet['sheet_label'],
                target_sheet_name=sheet['target_sheet_name']
            )


    # Method to close the browser after completing tasks  
    def close_browser(self):
        print("Closing the browser...")
        self.driver.quit()
