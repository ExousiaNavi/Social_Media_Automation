import asyncio
import os
import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from datetime import datetime, timedelta
from functools import partial

# class GoogleSheetManager:
#     logging.basicConfig(level=logging.INFO)

#     def __init__(self, json_keyfile_name, sheet_url, worksheet_name):
#         """
#         Initialize Google Sheet Manager with credentials and access to the Google Sheet.

#         :param json_keyfile_name: Name of the JSON key file for Google service account credentials (in the same directory).
#         :param sheet_url: The URL of the Google Sheet.
#         :param worksheet_name: The name of the worksheet to work with.
#         """
#         # Get the current script directory and construct the keyfile path
#         self.json_keyfile_path = os.path.join(os.path.dirname(__file__), json_keyfile_name)
#         self.sheet_url = sheet_url
#         self.worksheet_name = worksheet_name
#         self.client = None
#         self.worksheet = None
#         self.letter = None
#         # Set up Google Sheets API credentials
#         self._setup_credentials()

#     def _setup_credentials(self):
#         """
#         Set up the Google Sheets API credentials and authorize the client.
#         """
#         scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
#         creds = ServiceAccountCredentials.from_json_keyfile_name(self.json_keyfile_path, scope)
#         self.client = gspread.authorize(creds)

#         # Open the Google Sheet and worksheet
#         self.sheet = self.client.open_by_url(self.sheet_url)
#         self.worksheet = self.sheet.worksheet(self.worksheet_name)
#         logging.info(f"Connected to Google Sheet: {self.sheet_url}, Worksheet: {self.worksheet_name}")

#     def get_all_data(self):
#         """
#         Fetch all the data from the worksheet.
#         """
#         return self.worksheet.get_all_values()

#     def index_to_letter(self, index):
#         """
#         Convert a column index to its corresponding letter (A, B, C...).
        
#         :param index: The index of the column (0-based).
#         :return: The corresponding column letter (A, B, C...).
#         """
#         letter = ''
#         while index >= 0:
#             letter = chr((index % 26) + 65) + letter
#             index = index // 26 - 1
#         return letter
    
#     def letter_to_index(self, letter):
#         """
#         Convert a column letter (e.g., A, B, C) into a 0-based column index.
#         """
#         index = 0
#         for i, char in enumerate(reversed(letter)):
#             index += (string.ascii_uppercase.index(char) + 1) * (26 ** i)
#         return index - 1  # 0-based index
    
    
#     def extract_post_id(self, post_link):
#         """
#         Extract the post ID from a post link.

#         :param post_link: The full post link.
#         :return: The post ID extracted from the link.
#         """
#         return post_link.split('/')[-1]
    
    
#     def find_column_indices(self, header_row, columns):
#         """
#         Find the indices of the desired columns in the header row.

#         :param header_row: The header row of the worksheet.
#         :param columns: A list of column names to find in the header row.
#         :return: A dictionary mapping column names to their indices.
#         """
       
#         for column in columns:
#             try:
#                 index = header_row.index(column)
#                 logging.info(f"Index of '{column}': {index} (Letter: {self.index_to_letter(index)})")
#             except ValueError as e:
#                 logging.error(f"Column '{column}' not found: {e}")
#         return self.index_to_letter(index)


#     def find_post_id_in_column(self,sheet_manager, post_id, column_letter):
#         """
#         Search for a post_id in the specified column letter (e.g., 'K') starting from row 2.
        
#         :param sheet_manager: Instance of GoogleSheetManager
#         :param post_id: The post ID to search for.
#         :param column_letter: The column letter where the post_id is located.
#         :return: The row number where the post_id is found, or None if not found.
#         """
#         # Convert the column letter to an index (0-based)
#         column_index = sheet_manager.letter_to_index(column_letter)

#         # Get all data starting from row 2 and below
#         data = sheet_manager.get_all_data()[1:]  # Skip the header row
        
#         # Iterate through the rows starting from row 2 (index 1 in the data)
#         for row_number, row in enumerate(data, start=2):
#             try:
#                 # Extract the post_id from the specific column
#                 post_link = row[column_index]
#                 extracted_post_id = sheet_manager.extract_post_id(post_link)
                
#                 # Check if the extracted post_id matches the target post_id
#                 if extracted_post_id == str(post_id):
#                     logging.info(f"Post ID {post_id} found in row {row_number}")
#                     return row_number  # Return the 1-based row number where the post_id is found
#             except IndexError:
#                 # Handle case where the row is shorter than expected (missing columns)
#                 logging.error(f"Row {row_number} does not have enough columns.")
#                 continue
        
#         logging.info(f"Post ID {post_id} not found.")
#         return None
    

#     def retrieve_column_data(self, data, indices):
#         """
#         Retrieve data for specific columns from the worksheet data.

#         :param data: All data fetched from the worksheet.
#         :param indices: A dictionary of column indices to retrieve.
#         :return: A dictionary mapping column names to their corresponding values in the worksheet.
#         """
#         try:
#             retrieved_data = {
#                 'post_links': [row[indices['POST LINK']] for row in data[1:]],  # Skip the header
#                 'views_day3': [row[indices['Views Day 3']] for row in data[1:]],
#                 'reactions_day3': [row[indices['Reactions Day 3']] for row in data[1:]],
#                 'views_day7': [row[indices['Views Day 7']] for row in data[1:]],
#                 'reactions_day7': [row[indices['Reactions Day 7']] for row in data[1:]],
#                 'views_day30': [row[indices['Views Day 30']] for row in data[1:]],
#                 'reactions_day30': [row[indices['Reactions Day 30']] for row in data[1:]],
#             }
#             return retrieved_data
#         except IndexError as e:
#             logging.error(f"Error retrieving data: {e}")
#             return None

#     def map_post_ids_to_indices(self, post_links):
#         """
#         Create a mapping of post IDs to their row indices in the worksheet.

#         :param post_links: A list of post links.
#         :return: A dictionary mapping post IDs to their 1-based row indices.
#         """
#         return {self.extract_post_id(link): index + 2 for index, link in enumerate(post_links)}  # +2 for 1-based index and header

#     def extract_post_id(self, post_link):
#         """
#         Extract the post ID from a post link.

#         :param post_link: The full post link.
#         :return: The post ID extracted from the link.
#         """
#         return post_link.split('/')[-1]

#     # Insert data into a specific cell in the Google Sheet
#     def insert_data_in_cell(self, sheet_manager, row_index, column_letter, value):
#         """
#         Insert data into a specific cell in the Google Sheet based on the row index and column letter.
        
#         :param sheet_manager: Instance of GoogleSheetManager.
#         :param row_index: The row index where the data will be inserted (1-based index).
#         :param column_letter: The letter of the column where the data will be inserted (e.g., 'K').
#         :param value: The value to be inserted into the cell.
#         """
#         cell_reference = f"{column_letter}{row_index}"
#         logging.info(f"Inserting data into cell {cell_reference}: {value}")
#         sheet_manager.worksheet.update(cell_reference, value)
        
# # Example Usage:

# # Initialize the GoogleSheetManager
# sheet_manager = GoogleSheetManager(
#     json_keyfile_name='gs.json',
#     sheet_url="https://docs.google.com/spreadsheets/d/1mnGUYM54ssRtfkCVpC7TMSVAb9aR4Bx1qajXPEOmcCQ/edit?gid=882049161#gid=882049161",
#     worksheet_name="Telegram"
# )

# # Fetch all data
# data = sheet_manager.get_all_data()

# # Find the column indices
# header_row = data[0]
# columns_to_find = ['POST LINK']
# indices = sheet_manager.find_column_indices(header_row, columns_to_find)

# logging.info(f"Link Letter: {indices}")
# row_index = sheet_manager.find_post_id_in_column(sheet_manager, 1455, indices)

# if row_index:
#     logging.info(f"Post ID {1443} found in row {row_index}")
#     columns_to_find = ['Views Day 3']
#     indices = sheet_manager.find_column_indices(header_row, columns_to_find)

#     logging.info(f"Target Letter: {indices}{row_index}")
    
#      # Insert the value into the found row and column
#     sheet_manager.insert_data_in_cell(sheet_manager, row_index, indices, 5000)  # Example value: 5000
# else:
#     logging.info(f"Post ID {1443} not found.")
    
#version 2
class GoogleSheetsManager:
    logging.basicConfig(level=logging.INFO)
    def __init__(self, service_account_file: str, scopes: list[str], spreadsheet_id: str, platform: str, views_and_reactions: list[str], keyword: str, target_column: str, post_id: str):
        self.service_account_file = service_account_file
        self.scopes = scopes
        self.spreadsheet_id = spreadsheet_id
        self.platform = platform
        self.views_and_reactions = views_and_reactions
        self.keyword = keyword
        self.target_column = target_column
        self.post_id = post_id
        # Construct the full path to the JSON keyfile
        # self.json_keyfile_path = os.path.join(os.path.dirname(__file__), '../gsjson', self.json_keyfile_name)

        # self.clicks_imprs = clicks_imprs
        # Initialize credentials and create a service object
        self.creds = service_account.Credentials.from_service_account_file(
            self.service_account_file, scopes=self.scopes
        )
        self.service = build("sheets", "v4", credentials=self.creds)
        
    def col_number_to_letter(self, col):
        """Convert a zero-based column number to an Excel-style letter representation."""
        letter = ""
        while col >= 0:
            letter = chr(col % 26 + ord('A')) + letter
            col = col // 26 - 1
        return letter
    
    def extract_post_id(self,link):
        """Extract post ID from a Telegram link."""
        return link.split('/')[-1]  # Get the last segment of the URL


    def link_column(self, values, post_id_or_link, target_col_index):
        """Find the row index of a specific post ID or URL in the column values."""
        logging.info(f"Searching for post ID or link: {post_id_or_link}")

        post_id = None

        # Check if the input is a full link or a post ID
        if 'https://' in post_id_or_link:
            post_id = self.extract_post_id(post_id_or_link)  # Extract the post ID if the input is a full link
        else:
            post_id = str(post_id_or_link)  # If it's already a post ID, convert it to a string

        logging.info(f"Extracted post ID: {post_id}")

        # Iterate over each row to find the post link or post ID
        for row_index, row in enumerate(values):
            # If the row has fewer columns, pad it with None up to the target column index
            if len(row) <= target_col_index:
                row.extend([None] * (target_col_index - len(row) + 1))

            # Clean the value in the target column by stripping spaces and converting to lowercase
            link_value = row[target_col_index].strip().lower() if row[target_col_index] is not None else ""

            # Remove spaces and make lowercase from post_id for comparison
            post_id_clean = post_id.replace(" ", "").lower()

            # Check if the cleaned post ID or link is in the value
            if post_id_clean in link_value or post_id_or_link.lower() in link_value:
                logging.info(f"Found post/link '{post_id_or_link}' in row {row_index + 1}")
                return row_index + 1  # Return the 1-based row index

        logging.info(f"Post ID or link '{post_id_or_link}' not found.")
        return None

        
    def locate_header_index(self, header_row, column_header):
        """
        Find the index of a target column in the header row after removing spaces and converting to lowercase.

        :param header_row: The header row to search through.
        :param target_column: The target column to find (after normalization).
        :return: The index of the target column if found, otherwise -1.
        """
        # Normalize the target column by removing spaces and converting to lowercase
        normalized_target_column = column_header.replace(" ", "").lower()
        # Loop through the header row and normalize each column header for comparison
        for index, column in enumerate(header_row):
            normalized_column = column.replace(" ", "").lower()
            # logging.info(f"checking header: {normalized_target_column} = {normalized_column}")
            if normalized_column == normalized_target_column:
                # logging.info(f"Target column found: {column_header}, index: {index}")
                return index
            
        
        logging.error(f"Target column '{column_header}' not found in header.")
        return -1  # Return -1 if the column is not found
    
    async def run(self):
        """Find the target substring, get values below in the same column, and update a cell."""
        try:
            # Fetch all sheet data asynchronously
            result = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.service.spreadsheets().values().get(
                    spreadsheetId=self.spreadsheet_id,
                    range=f"{self.platform}!A1:ZZ"
                ).execute()  # Ensure to call .execute()
            )
            values = result.get("values", [])
            # logging.info(values)
            if not values:
                print("No data found.")
                return
            
             # Extract the header row and find the column index 
            header_row = values[0]
            logging.info(f"Header Row: {header_row}")
            
            target_col_index = None
            target_col_keyword = None
            # target_col_postid = None
            target_col_index = self.locate_header_index(header_row, self.target_column)
            
            # Logging the column letter and values
            col_letter = self.col_number_to_letter(target_col_index)
            
            # target_col_index = None
            target_col_keyword = self.locate_header_index(header_row, self.keyword)
            # Logging the column letter and values
            col_letter_keyword = self.col_number_to_letter(target_col_keyword)
            
            logging.info(f"Column letter for {self.target_column}: {col_letter}")
            
            # target_col_postid = self.locate_header_index(header_row, 'postid')
            
            # # Logging the column letter and values
            # col_letter_postid = self.col_number_to_letter(target_col_postid)
            
            # logging.info(f"Column values below header: {column_values_below}")

            # Find the post ID or link in the column (e.g., search for 'https://t.me/baji_bgd/1442')
            # post_id_or_link = "1442"  # You can replace with a post ID or a link
            row_position = self.link_column(values, self.post_id, target_col_index)
            
            logging.info(f"rowPosition: {row_position}")
            if row_position is None:
                return

            # Construct the range in A1 notation for updating
            cell_range = f"{self.platform}!{col_letter_keyword}{row_position}"

            logging.info(f"cell rangeL {cell_range}")
            # Prepare the body with values to update
            body = {
                "values": [
                    self.views_and_reactions
                ]
            }

            # # Update the cell in the sheet asynchronously
            await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.service.spreadsheets().values().update(
                    spreadsheetId=self.spreadsheet_id,
                    range=cell_range,
                    valueInputOption="USER_ENTERED",
                    body=body
                ).execute()  # Ensure to call .execute()
            )

            data = {
                "post_id": self.post_id,
                "status": 200,
                "text": self.platform+" Automation Completed",
                "title": "Spreadsheet Automation Completed!",
                "icon": "success",
                "time": datetime.now().strftime("%I:%M %p"),
                "platform": self.platform,
                "keyword": self.keyword
            }
            return data
        except HttpError as err:
            print(err)
            
            

# # Function to run async code
# async def main():
#     # Initialize the GoogleSheetsManager for the general bo_data processing
#     gmanager = GoogleSheetsManager(
#         '../gs.json',  # Adjust path if needed
#         ["https://www.googleapis.com/auth/spreadsheets"],
#         '1mnGUYM54ssRtfkCVpC7TMSVAb9aR4Bx1qajXPEOmcCQ',  # Spreadsheet ID
#         'Telegram',  # Worksheet name
#         [5000, 5000],  # Example BO data
#         'Views Day 7',  # Keyword to search for
#         'POST LINK',  # Target column to update
#         '1443'
#     )
    
#     await gmanager.run()


# # Run the async main function
# if __name__ == "__main__":
#     asyncio.run(main())