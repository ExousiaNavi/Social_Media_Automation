from twitter.bjsports_twitter_bot import BjsportsBot
import time
# This class contains test cases to automate Telegram actions
class BJSportsTwitterAutomation:
    def __init__(self):
        # Create an instance of the TelegramBot class
        self.bjsports_twitter_automation = BjsportsBot()

    # Method to run a series of Telegram Web test cases
    def run_tests(self):
        print("Running Twitter tests...")
        # Log into Telegram using a phone number
        self.bjsports_twitter_automation.automate_task()
        time.sleep(5)
        # Close the browser after the test is complete
        self.bjsports_twitter_automation.close_browser()




