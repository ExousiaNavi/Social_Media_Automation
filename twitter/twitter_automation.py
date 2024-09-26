from twitter.twitter_bot import TwitterBot
import time
# This class contains test cases to automate Telegram actions
class TwitterAutomation:
    def __init__(self):
        # Create an instance of the TelegramBot class
        self.twitter_bot = TwitterBot()

    # Method to run a series of Telegram Web test cases
    def run_tests(self):
        print("Running Twitter tests...")
        # Log into Telegram using a phone number
        self.twitter_bot.automate_task()
        time.sleep(5)
        # Close the browser after the test is complete
        self.twitter_bot.close_browser()




