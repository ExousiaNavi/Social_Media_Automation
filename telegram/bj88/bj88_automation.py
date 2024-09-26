from telegram.bj88.bj88_bot import AsyncBrowserAutomation
import time
# This class contains test cases to automate Telegram actions
class BJ88Automation:
    def __init__(self):
        # Create an instance of the TelegramBot class
        self.telegram_bot = AsyncBrowserAutomation(headless=False)

    # Method to run a series of Telegram Web test cases
    async def run_tests(self):
        print("Running Telegram tests...")
        # Log into Telegram using a phone number
        await self.telegram_bot.start_browser()
        # Close the browser after the test is complete
        await self.telegram_bot.close_browser()