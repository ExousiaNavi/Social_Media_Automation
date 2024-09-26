from twitter.jeetbuzz_twitter_bot import JeetBuzzTwitterBot
import time
# This class contains test cases to automate Telegram actions
class JeetBuzzTwitterAutomation:
    def __init__(self):
        # Create an instance of the TelegramBot class
        self.jeetbuzz_twitter_bot = JeetBuzzTwitterBot()

    # Method to run a series of Telegram Web test cases
    def run_tests(self):
        print("Running Twitter tests...")
        # Log into Telegram using a phone number
        self.jeetbuzz_twitter_bot.automate_task()
        time.sleep(5)
        # Close the browser after the test is complete
        self.jeetbuzz_twitter_bot.close_browser()




