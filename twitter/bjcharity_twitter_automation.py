from twitter.bjcharity_twitter_bot import BJCharityBot
import time
# This class contains test cases to automate Telegram actions
class BJCharityTwitterAutomation:
    def __init__(self):
        # Create an instance of the TelegramBot class
        self.bjcharity_twitter_automation = BJCharityBot()

    # Method to run a series of Telegram Web test cases
    def run_tests(self):
        print("Running Twitter tests...")
        # Log into Telegram using a phone number
        self.bjcharity_twitter_automation.automate_task()
        time.sleep(5)
        # Close the browser after the test is complete
        self.bjcharity_twitter_automation.close_browser()




