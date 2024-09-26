from selenium import webdriver

# This class is responsible for managing the browser WebDriver instance
class Browser:
    def __init__(self):
        # Placeholder for the WebDriver object
        self.driver = None

    # Method to get or initialize the WebDriver instance
    def get_driver(self):
        if self.driver is None:
            print("Initializing WebDriver...")
            # Initialize the WebDriver (in this case, Chrome)
            self.driver = webdriver.Chrome()  # Use the appropriate driver for your browser
        return self.driver
