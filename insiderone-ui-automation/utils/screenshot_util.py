
import os
import time
from selenium.webdriver.common.by import By

class ScreenshotUtil:
    def __init__(self, driver, screenshot_dir):
        self.driver = driver
        self.screenshot_dir = screenshot_dir

    def capture_screenshot(self, test_name):
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_path = os.path.join(self.screenshot_dir, f'{test_name}_{timestamp}.png')
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path
