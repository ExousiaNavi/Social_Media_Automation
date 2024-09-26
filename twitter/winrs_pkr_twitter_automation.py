from twitter.winrs_pkr_twitter_bot import WinrsPKRTwitterBot
import time
# This class contains test cases to automate Telegram actions
class WinPKRTwitterAutomation:
    def __init__(self):
        # Create an instance of the TelegramBot class
        self.winrs_pkr_twitter_bot = WinrsPKRTwitterBot()

    # Method to run a series of Telegram Web test cases
    def run_tests(self):
        print("Running Twitter tests...")
        # Log into Telegram using a phone number
        self.winrs_pkr_twitter_bot.automate_task()
        time.sleep(5)
        # Close the browser after the test is complete
        self.winrs_pkr_twitter_bot.close_browser()




