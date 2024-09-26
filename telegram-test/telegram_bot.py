from selenium import webdriver
from utilities.browser import Browser

# This class contains the Selenium actions to automate Telegram Web
class TelegramBot:
    def __init__(self):
         # Get the Selenium WebDriver instance from the Browser class
        self.driver = Browser().get_driver()
        
    # Method to open Telegram Web using Selenium
    def open_telegram_web(self):
        print("Opening Telegram web...")
        # Navigate to Telegram Web
        self.driver.get("https://web.telegram.org")

    # Method to log into Telegram with a phone number
    def login(self, phone_number):
        print("Logging in with phone number:", phone_number)
        # Implement login steps using Selenium here
        # Placeholder: Add logic for entering phone number and submitting login form
    
    # Method to close the browser after completing tasks  
    def close_browser(self):
        print("Closing the browser...")
        self.driver.quit()
