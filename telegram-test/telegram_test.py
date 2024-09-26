from telegram.telegram_bot import TelegramBot
import time
# This class contains test cases to automate Telegram actions
class TelegramTest:
    def __init__(self):
        # Create an instance of the TelegramBot class
        self.telegram_bot = TelegramBot()

    # Method to run a series of Telegram Web test cases
    def run_tests(self):
        print("Running Telegram tests...")
        # Open Telegram Web
        self.telegram_bot.open_telegram_web()
        # Log into Telegram using a phone number
        self.telegram_bot.login("Telegram Login here...")
        time.sleep(5)
        # Close the browser after the test is complete
        self.telegram_bot.close_browser()
