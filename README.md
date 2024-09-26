platform/
│
├── main.py                 # Entry point for the platform
├── platform.py             # Platform class to manage dynamic test execution
├── telegram/
│   ├── __init__.py
│   ├── telegram_bot.py      # Telegram-specific Selenium actions
│   ├── telegram_test.py     # Telegram-specific tests
├── facebook/
│   ├── __init__.py
│   ├── facebook_bot.py      # Facebook-specific Selenium actions
│   ├── facebook_test.py     # Facebook-specific tests
├── utilities/
│   ├── __init__.py
│   ├── browser.py           # Manages WebDriver setup
│   ├── base_page.py         # Base page class with common methods (click, find, etc.)
└── venv/                   # Virtual environment folder

virtual environment
command : python -m venv venv