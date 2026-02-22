"""
Creates a Selenium WebDriver for the chosen browser (Chrome or Firefox).

Expects ChromeDriver (for Chrome) and GeckoDriver (for Firefox) to be installed
and available on the system PATH. Browser from config.json ("browser") or env BROWSER.
"""
from selenium import webdriver

from utils.config_loader import get_browser


class DriverManager:
    def __init__(self, browser=None):
        """Browser: passed in, or from config (BROWSER env / config.json). Normalized to 'chrome' or 'firefox'."""
        self.browser = (browser or get_browser()).strip().lower()
        self.driver = None

    def start_driver(self):
        if self.browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=options)
        elif self.browser == "firefox":
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Browser {self.browser!r} is not supported.")
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
