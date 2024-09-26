import time
import asyncio
class Platform:
    def __init__(self):
        self.platform_tests = []

    def add_platform_test(self, test_method):
        self.platform_tests.append(test_method)

    async def run_test(self, test):
        # Check if the test method is an async function
        if asyncio.iscoroutinefunction(test):
            # If the test is async, await it
            await test()
        else:
            # If the test is sync, just call it
            test()

    async def run_all_tests(self, wait_time=5):
        for index, test in enumerate(self.platform_tests):
            print(f"Starting platform test {index + 1}...")

            # Call the test, handle both async and sync
            await self.run_test(test)

            print(f"Completed platform test {index + 1}")
            
            if index < len(self.platform_tests) - 1:
                print(f"Waiting {wait_time} seconds before starting next test...")
                # Use asyncio.sleep to wait asynchronously
                await asyncio.sleep(wait_time)
