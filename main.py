from platform_controller import Platform
from telegram.telegram_automation import TelegramAutomation
from facebook.facebook_automation import FacebookAutomation
from twitter.twitter_automation import TwitterAutomation
from telegram.bj88.bj88_automation import BJ88Automation
from twitter.jeetbuzz_twitter_automation import JeetBuzzTwitterAutomation
from twitter.six6s_twitter_automation import Six6xTwitterAutomation
from twitter.bjcharity_twitter_automation import BJCharityTwitterAutomation
from twitter.bjsports_twitter_automation import BJSportsTwitterAutomation
import asyncio
# Entry point for the platform
if __name__ == "__main__":
    # Create an instance of the Platform class
    platform = Platform()

    # Facebook Embbed
    # platform.add_platform_test(FacebookAutomation().run_tests)

    # Telegram
    platform.add_platform_test(TelegramAutomation().run_tests)
    #bj88
    # platform.add_platform_test(BJ88Automation().run_tests)

    # Twitter
    # platform.add_platform_test(TwitterAutomation().run_tests)
    # platform.add_platform_test(JeetBuzzTwitterAutomation().run_tests)
    # platform.add_platform_test(Six6xTwitterAutomation().run_tests)
    # platform.add_platform_test(BJCharityTwitterAutomation().run_tests)
    # platform.add_platform_test(BJSportsTwitterAutomation().run_tests)





    # platform.add_platform_test(JeetBuzzAutomation().run_tests)




    # Run all tests consecutively with a 5-second pause between each test
     # Use asyncio.run to properly await the asynchronous method
    asyncio.run(platform.run_all_tests(wait_time=5))
