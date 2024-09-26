import time

class Platform:
    def __init__(self):
        self.platform_tests = []

    def add_platform_test(self, test_method):
        self.platform_tests.append(test_method)

    def run_all_tests(self, wait_time=5):
        for index, test in enumerate(self.platform_tests):
            print(f"Starting platform test {index + 1}...")
            test()
            print(f"Completed platform test {index + 1}")
            if index < len(self.platform_tests) - 1:
                print(f"Waiting {wait_time} seconds before starting next test...")
                time.sleep(wait_time)
