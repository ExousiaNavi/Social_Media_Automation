import asyncio
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from datetime import datetime, timedelta
from functools import partial

class GoogleSheetsManager:
    def __init__(self, service_account_file: str, scopes: list[str], spreadsheet_id: str, platform: str, bo: list[str], keyword: str, target_date: str):
        self.service_account_file = service_account_file
        self.scopes = scopes
        self.spreadsheet_id = spreadsheet_id
        self.platform = platform
        self.bo = bo
        self.keyword = keyword
        self.target_date = target_date
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

    def formatTime(self, values):
        if isinstance(values, datetime):
            # If it's already a datetime object, return it
            return values
        elif isinstance(values, str):
            date_string = values

            try:
                # Try parsing the date string in 'YYYY/MM/DD' format
                date_obj = datetime.strptime(date_string, '%Y/%m/%d')
                return date_obj
            except ValueError:
                try:
                    # If the first format fails, try 'YYYY-MM-DD' format
                    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
                    return date_obj
                except ValueError:
                    # If both formats fail, return None
                    return None
        else:
            return None
    
    def yesterday_date(self, values):
        """Find the row index of yesterday's date."""
        # yesterday_date = datetime.now().date()
        # If no target date is provided, default to yesterday
        yesterday_date = self.formatTime(self.target_date)
        if yesterday_date is None:
            yesterday_date = (datetime.now().date() - timedelta(days=1))
            
        formatted_date = yesterday_date.strftime("%B %#d")
        yesterday_date_no_zero = yesterday_date.strftime("%#m/%#d/%Y")
        print(f"data: {yesterday_date_no_zero}, {formatted_date}")
        yesterdays_date_row_index = None
        for row_index, row in enumerate(values):
            if row and len(row) > 0:
                row_date = row[0]
                if row_date == formatted_date or row_date == yesterday_date_no_zero:
                    yesterdays_date_row_index = row_index
                    break

        if yesterdays_date_row_index is not None:
            print(f"Yesterday's date '{yesterday_date_no_zero}' found in row {yesterdays_date_row_index + 1}")
            return yesterdays_date_row_index
        else:
            print(f"Yesterday's date '{yesterday_date_no_zero}' not found.")
            return None

    def get_matched_keyword(self, keyw):
        # Check if the provided keyword is in the array
        if keyw  == 'Baji (adcash)':
            return 'adcash'
        if keyw == 'Baji (jbclickadubdt)':
            return 'jbclickadubdt'
        if keyw == 'Baji (jbtrafficstars)':
            return 'jbtrafficstars'
        if keyw == 'Six6s (s6clickadubdt)':
            return 's6clickadubdt'
        else:
            return keyw  # or any default value you'd prefer
        
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

            if not values:
                print("No data found.")
                return

            target_row_index = None
            target_col_index = None
            for row_index, row in enumerate(values):
                for col_index, cell in enumerate(row):
                    if self.keyword in cell:
                        target_row_index = row_index
                        target_col_index = col_index
                        break
                if target_row_index is not None:
                    break

            if target_row_index is None or target_col_index is None:
                print(f"'{self.keyword}' not found in the sheet.")
                return

            # Get all values in the target column below the target row
            column_values_below = []
            for row_index in range(target_row_index + 1, len(values)):
                if len(values[row_index]) > target_col_index:
                    column_values_below.append(values[row_index][target_col_index])

            col_letter = self.col_number_to_letter(target_col_index)

            # Find yesterday's date row index
            rowPositionYesterday = self.yesterday_date(values)
            if rowPositionYesterday is None:
                return

            # Construct the range in A1 notation for updating
            cell_range = f"{self.platform}!{col_letter}{rowPositionYesterday + 1}"

            # Prepare the body with values to update
            body = {
                "values": [
                    self.bo
                ]
            }

            # Update the cell in the sheet asynchronously
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
                "target_date": self.target_date,
                "status": 200,
                "text": self.platform+" Automation Completed",
                "title": "Spreadsheet Automation Completed!",
                "icon": "success",
                "time": datetime.now().strftime("%I:%M %p"),
                "platform": self.platform,
                "keyword": self.get_matched_keyword(self.keyword)
            }
            return data
        except HttpError as err:
            print(err)
