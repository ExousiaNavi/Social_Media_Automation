from telegram.telegram_bot import TelegramBot
import time
# This class contains test cases to automate Telegram actions
class TelegramAutomation:
    def __init__(self):
        # Create an instance of the TelegramBot class
        self.telegram_bot = TelegramBot()

    # Method to run a series of Telegram Web test cases
    async def run_tests(self):
        print("Running Telegram tests...")
        # Log into Telegram using a phone number
        await self.telegram_bot.run()
        time.sleep(5)
        # Close the browser after the test is complete
        # self.telegram_bot.close_browser()




