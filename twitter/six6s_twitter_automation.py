from twitter.six6s_twitter_bot import Six6sTwitterBot
import time
# This class contains test cases to automate Telegram actions
class Six6xTwitterAutomation:
    def __init__(self):
        # Create an instance of the TelegramBot class
        self.six6s_twitter_bot = Six6sTwitterBot()

    # Method to run a series of Telegram Web test cases
    def run_tests(self):
        print("Running Twitter tests...")
        # Log into Telegram using a phone number
        self.six6s_twitter_bot.automate_task()
        time.sleep(5)
        # Close the browser after the test is complete
        self.six6s_twitter_bot.close_browser()




