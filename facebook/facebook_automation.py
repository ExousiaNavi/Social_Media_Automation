from facebook.facebook_bot import FacebookBot
import time
# This class contains test cases to automate Facebook actions
class FacebookAutomation:
    def __init__(self):
        # Create an instance of the TelegramBot class
        self.facebook_bot = FacebookBot()

    # Method to run a series of Facebook Web test cases
    def run_tests(self):
        print("Running Facebook tests...")
        
        # Open Facebook Web
        self.facebook_bot.automate_task()
       
