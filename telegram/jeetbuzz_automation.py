from telegram.jeetbuzz_bot import JeetBuzzBot
import time
# This class contains test cases to automate Telegram actions
class JeetBuzzAutomation:
    def __init__(self):
        # Create an instance of the TelegramBot class
        self.jeetbuzz_bot = JeetBuzzBot()

    # Method to run a series of Telegram Web test cases
    def run_tests(self):
        print("Running Telegram tests...")
        # Log into Telegram using a phone number
        self.jeetbuzz_bot.automate_task()
        time.sleep(5)
        # Close the browser after the test is complete
        self.jeetbuzz_bot.close_browser()




