from selenium import webdriver
from utilities.browser import Browser
import requests
from googleapiclient.discovery import build
from google.oauth2 import service_account
from playwright.sync_api import sync_playwright
import re

SERVICE_ACCOUNT_FILE = r'C:\Users\BJ-LAP-65\Downloads\platform\performance-424301-244a41249704.json'

class FacebookBot:
    def __init__(self):
        self.driver = Browser().get_driver()
        # Use a single path for all service files
        self.service_file = SERVICE_ACCOUNT_FILE
        self.services = {
            key: self.build_service(self.service_file) 
            for key in ['pkr', 'bdt','inr', 'npr',]
        }

    @staticmethod
    def build_service(service_account_file):
        credentials = service_account.Credentials.from_service_account_file(
            service_account_file,
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        return build('sheets', 'v4', credentials=credentials)

    @staticmethod
    def get_hyperlinks(service, spreadsheet_id, range_name):
        try:
            sheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=range_name, includeGridData=True).execute()
            data = sheet['sheets'][0]['data'][0]['rowData']
        except Exception as e:
            print(f"An error occurred: {e}")
            return [], []

        urls, row_numbers = [], []
        for i, row in enumerate(data):
            for cell in row.get('values', []):
                if 'userEnteredFormat' in cell and 'textFormat' in cell['userEnteredFormat']:
                    text_format = cell['userEnteredFormat']['textFormat']
                    if 'link' in text_format and 'uri' in text_format['link']:
                        urls.append(text_format['link']['uri'])
                        row_numbers.append(i + 1)  # Rows are 1-indexed in Sheets
        return urls, row_numbers

    @staticmethod
    def extract_post_id(content, pattern):
        match = re.search(pattern, content)
        return match.group(0).split('/')[-1] if match else None

    @staticmethod
    def update_google_sheet(service, spreadsheet_id, row_number, post_id, write_column):
        range_name = f"Facebook!{write_column}{row_number}:{write_column}{row_number}"
        values = [[post_id]] if post_id is not None else [[]]
        body = {'values': values}
        print(f"Updating sheet at range: {range_name} with values: {values}")
        try:
            service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id, range=range_name,
                valueInputOption="RAW", body=body).execute()
            print(f"Updated cell at row {row_number} with Post ID: {post_id}")
        except Exception as e:
            print(f"Failed to update Google Sheet: {e}")

    @staticmethod
    def get_existing_values(service, spreadsheet_id, column, row_numbers):
        range_name = f"Facebook!{column}1:{column}{max(row_numbers)}"
        try:
            result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
            values = result.get('values', [])
            return {i + 1: values[i][0] if i < len(values) and values[i] else '' for i in range(len(row_numbers))}
        except Exception as e:
            print(f"Failed to get existing values: {e}")
            return {}

    def automate_facebook_embed(self, service, spreadsheet_id, urls, row_numbers, existing_values, write_column, extractors):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            for url, row in zip(urls, row_numbers):
                if existing_values.get(row):
                    print(f"Row {row} is already processed. Skipping...")
                    continue

                post_id_printed = False

                def handle_request(request):
                    nonlocal post_id_printed
                    if "https://developers.facebook.com/plugins/code?path=post" in request.url and not post_id_printed:
                        try:
                            response = request.response()
                            if response and response.status == 200:
                                response_body = response.text()

                                post_id = None
                                for extractor in extractors:
                                    post_id = extractor(response_body)
                                    if post_id:
                                        break

                                if post_id:
                                    print(f"Post ID: {post_id}")
                                    self.update_google_sheet(service, spreadsheet_id, row, post_id, write_column)
                                else:
                                    print(f"No valid ID found for URL: {url}")

                                post_id_printed = True
                        except Exception as e:
                            print(f"Failed to retrieve response for {url}: {e}")

                page.on("requestfinished", handle_request)
                page.goto("https://developers.facebook.com/docs/plugins/embedded-posts/")
                
                input_field = page.wait_for_selector('//*[@id="param_href"]', timeout=20000)
                input_field.fill(url)

                first_get_code_button = page.wait_for_selector('._42ft._4jy0._4jy4._4jy1.selected._51sy', timeout=20000)
                first_get_code_button.click()

                second_get_code_button = page.wait_for_selector('._42ft._4jy0._4jy4._4jy1.selected._51sy', timeout=20000)
                second_get_code_button.click()

                page.wait_for_selector('pre', timeout=20000)

                try:
                    if not post_id_printed:
                        specific_content = page.locator('//*[@id="u_5_3_CC"]/pre').text_content(timeout=5000)
                        print(f"Specific content found: {specific_content}")

                        post_id = None
                        for extractor in extractors:
                            post_id = extractor(specific_content)
                            if post_id:
                                break

                        if post_id:
                            print(f"Post ID: {post_id}")
                            self.update_google_sheet(service, spreadsheet_id, row, post_id, write_column)
                        else:
                            print(f"No valid ID found for content: {specific_content}")
                except Exception as e:
                    print(f"Failed to locate content for {url}: {e}")

            browser.close()

    def process_sheet(self, key):
        constants = {
            'bdt': {
                'spreadsheet_id': '1I4pezDXdTjl1FysfpK6NZ8XDNQirlmkWFlDaEeDuhq4',
                'range_name': 'Facebook!K1:K1000',
                'write_column': 'AA',
                'read_column': 'K',
                'extractors': [
                    lambda content: self.extract_post_id(content, r'www\.facebook\.com\\/baji\.bgd\\/posts\\/\d+'),
                    lambda content: self.extract_post_id(content, r'www\.facebook\.com\\/groups\\/bajibangladesh\\/posts\\/(\d+)'),
                    lambda content: self.extract_post_id(content, r'www\.facebook\.com\\/baji\.bgd\\/videos\\/\d+'),
                    lambda content: self.extract_post_id(content, r'www\.facebook\.com\\/reel\\/(\d+)'),
                    lambda content: self.extract_post_id(content, r'www\.facebook\.com\\/groups\\/(\d+)')
                ]
            },
            'inr': {
                'spreadsheet_id': '1EZxME4AbBPmL50-wSsow-chc2QWyEWlTHbccpvde0uU',
                'range_name': 'Facebook!K1:K1000',
                'write_column': 'AB',
                'read_column': 'K',
                'extractors': [
                    lambda content: self.extract_post_id(content, r'www\.facebook\.com\\/baji\.inr\\/posts\\/(\d+)'),
                    lambda content: self.extract_post_id(content, r'www\.facebook\.com\\/baji\.inr\\/videos\\/\d+'),
                    lambda content: self.extract_post_id(content, r'www\.facebook\.com\\/groups\\/(?:baji\.in|baji\.ind|bajiindia)\\/permalink\\/\d+'),
                    lambda content: self.extract_post_id(content, r'www\.facebook\.com\\/groups\\/(?:baji\.in|baji\.ind|bajibangladesh)\\/posts\\/\d+'),
                    lambda content: self.extract_post_id(content, r'www\.facebook\.com\\/groups\\/(\d+)')
                ]
            },
            'npr': {
                'spreadsheet_id': '1xFVNpCgahVclVbjAdNj6frUgy1AOxSl1_UicJS6NXpE',
                'range_name': 'Facebook!K1:K1000',
                'write_column': 'AB',
                'read_column': 'K',
                'extractors': [
                    lambda content: self.extract_post_id(content, r'www\.facebook\.com\\/(?:baji\.npl|groups\\/baji\.npl|groups\\/baji\.np|reel)\\/(?:posts|permalink|videos|reel)\\/\d+'),
                    lambda content: self.extract_post_id(content, r'https:\/\/www\.facebook\.com\/(?:baji\.npl|groups\/baji\.npl|groups\/baji\.np|reel)\/(?:posts|permalink|videos|reel)\/\d'),
                ]
            },
            'pkr': {
                'spreadsheet_id': '1R62akcOHRB1LONQo-t2FYjRtz74goHZtyhKWOJTWCBQ',
                'range_name': 'Facebook!K1:K1000',
                'write_column': 'AB',
                'read_column': 'K',
                'extractors': [
                    lambda content: self.extract_post_id(content,r'www\.facebook\.com\\/baji\.pkr\\/posts\\/\d+'),
                    lambda content: self.extract_post_id(content,r'www\.facebook\.com\\/baji\.pkr\\/videos\\/\d+'),
                    lambda content: self.extract_post_id(content,r'www\.facebook\.com\\/groups\\/bajipakistan\\/permalink\\/(\d+)'),
                    lambda content: self.extract_post_id(content,r'www\.facebook\.com\\/groups\\/baji\.pk\\/permalink\\/(\d+)'),
                    lambda content: self.extract_post_id(content,r'www\.facebook\.com\\/groups\\/bajipakistan\\/posts\\/(\d+)'),
                    lambda content: self.extract_post_id(content,r'www\.facebook\.com\\/groups\\/baji\.pk\\/posts\\/(\d+)'),
                    lambda content: self.extract_post_id(content,r'www\.facebook\.com\\/reel\\/\d+'),
                    lambda content: self.extract_post_id(content,r'www\.facebook\.com\\/groups\\/baji\.pak\\/permalink\\/(\d+)'),
                ]
            }
        }

        constants_for_key = constants[key]
        urls, row_numbers = self.get_hyperlinks(self.services[key], constants_for_key['spreadsheet_id'], constants_for_key['range_name'])
        existing_values = self.get_existing_values(self.services[key], constants_for_key['spreadsheet_id'], constants_for_key['write_column'], row_numbers)
        self.automate_facebook_embed(
            self.services[key],
            constants_for_key['spreadsheet_id'],
            urls,
            row_numbers,
            existing_values,
            constants_for_key['write_column'],
            constants_for_key['extractors']
        )

    def automate_task(self):
        # Process all regions
        for key in ['pkr', 'bdt','inr','npr',]:
            self.process_sheet(key)

    def close_browser(self):
        print("Closing the browser...")
        self.driver.quit()
