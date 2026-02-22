"""Insider home page (https://insiderone.com/). Verify page is opened and all main blocks are loaded."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config_loader import get_base_url


class HomePage(BasePage):

    # URL and identity
    def __init__(self, driver):
        super().__init__(driver, base_url=get_base_url())

    LOCATOR_HEADER = (By.ID, "navigation")  # unique: <header id="navigation">
    LOCATOR_MAIN = (By.CSS_SELECTOR, "main.flexible-layout")  # unique: single <main>
    LOCATOR_HERO_H1 = (By.CSS_SELECTOR, "section.homepage-hero h1")  # unique: hero section has one h1
    LOCATOR_FOOTER = (By.ID, "footer")  # unique: <footer id="footer">

    # Main content sections (must be present when page is fully loaded)
    LOCATOR_HERO = (By.CSS_SELECTOR, "section.homepage-hero")
    LOCATOR_SOCIAL_PROOF = (By.CSS_SELECTOR, "section.homepage-social-proof")
    LOCATOR_CORE_DIFFERENTIATORS = (By.CSS_SELECTOR, "section.homepage-core-differentiators")
    LOCATOR_CAPABILITIES = (By.CSS_SELECTOR, "section.homepage-capabilities")
    LOCATOR_CHANNELS = (By.CSS_SELECTOR, "section.homepage-channels")
    LOCATOR_CASE_STUDY = (By.CSS_SELECTOR, "section.homepage-case-study")
    LOCATOR_ANALYST = (By.CSS_SELECTOR, "section.homepage-analyst")
    LOCATOR_INTEGRATIONS = (By.CSS_SELECTOR, "section.homepage-integrations")
    LOCATOR_RESOURCES = (By.CSS_SELECTOR, "section.homepage-resources")
    LOCATOR_CALL_TO_ACTION = (By.CSS_SELECTOR, "section.homepage-call-to-action")

    # All main blocks to wait for (header, main, hero h1, key sections, footer)
    MAIN_BLOCKS = [
        "LOCATOR_HEADER",
        "LOCATOR_MAIN",
        "LOCATOR_HERO_H1",
        "LOCATOR_HERO",
        "LOCATOR_SOCIAL_PROOF",
        "LOCATOR_CORE_DIFFERENTIATORS",
        "LOCATOR_CAPABILITIES",
        "LOCATOR_CHANNELS",
        "LOCATOR_CASE_STUDY",
        "LOCATOR_ANALYST",
        "LOCATOR_INTEGRATIONS",
        "LOCATOR_RESOURCES",
        "LOCATOR_CALL_TO_ACTION",
        "LOCATOR_FOOTER",
    ]

    def load(self):
        """Open home page."""
        self.driver.get(self.base_url)

    def is_opened(self):
        """Return True if the home page is open (current URL matches base URL)."""
        return self.driver.current_url == self.base_url

    def wait_for_main_blocks_loaded(self):
        """Wait until all main blocks are present in the DOM (page structure loaded)."""
        for name in self.MAIN_BLOCKS:
            locator = getattr(self, name)
            self.wait_for_element(locator)
