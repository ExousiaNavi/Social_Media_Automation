import asyncio
from playwright.async_api import async_playwright
class AsyncBrowserAutomation:
    def __init__(self, headless:bool = True):
        self.headless = headless

    async def start_browser(self):
        # Launch the browser
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            self.context = await browser.new_context()
            self.page = await self.context.new_page()
            
    async def visit_page(self, url: str):
        # Open the webpage
        if not hasattr(self, 'page'):
            raise Exception("Browser is not started. Call start_browser() first.")
        await self.page.goto(url)
        print(f"Visited {url}")
        
    async def close_browser(self):
        # Close the browser
        await self.context.close()