# BasePage class contains common Selenium actions that can be reused across different page objects
class BasePage:
    def __init__(self, driver):
        # Initialize with the Selenium WebDriver instance
        self.driver = driver
        
    # Method to find a web element by its locator
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    # Method to click on a web element
    def click(self, locator):
        element = self.find_element(locator)
        element.click()
        
    # Method to send text input to a web element
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)
