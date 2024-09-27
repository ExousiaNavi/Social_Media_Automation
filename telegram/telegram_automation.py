from telegram.telegram_bot import TelegramBot
import time
import os
import json
import logging
# This class contains test cases to automate Telegram actions
class TelegramAutomation:
    logging.basicConfig(level=logging.INFO)
    def __init__(self):
        # Create an instance of the TelegramBot class
        self.telegram_bot = TelegramBot()

    # Method to run a series of Telegram Web test cases
    async def run_tests(self):
        print("Running Telegram tests...")
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute path to the credentials.json file
        credentials_path = os.path.join(script_dir, "..", "credentials", "credentials.json")

        # Normalize the path (optional but good for cross-platform support)
        credentials_path = os.path.normpath(credentials_path)
        # Load the JSON data from a file
        with open(credentials_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    
        # Access the 'Baji' data for debug only
        # baji_data = data["data"][0]["Baji"]
        for item in data["data"]:
             # Loop through all the keys in the current item
            for key, value in item.items():
                logging.info(f"Key: {key}")
                # Check if 'credentials' exist in the current key's value
                if "credentials" in value:
                    credentials = value["credentials"]
                    
                    # Access the email and password directly
                    email = credentials.get("email", "")
                    password = credentials.get("password", "")
                    
                    # Only log if both email and password are non-empty
                    if (email and password) and (key == 'Baji'):
                        
                        if "currency_channels" in value:
                            channel = value["currency_channels"]
                            main_url = "https://telemetr.io/en"
                            for ch in channel:
                                # logging.info(f"currency channel: {ch.get('currency')}")
                                currency = ch.get("currency", "")
                                url = ch.get("url", "")
                                await self.telegram_bot.run(email, password, main_url, currency, url, key)
                        # Log into Telegram using a phone number
                        #main url
                        # main_url = "https://telemetr.io"
                        
                        # await self.telegram_bot.run(email, password, main_url, )
        # Log into Telegram using a phone number
        # await self.telegram_bot.run()
        time.sleep(5)
        # Close the browser after the test is complete
        # self.telegram_bot.close_browser()




