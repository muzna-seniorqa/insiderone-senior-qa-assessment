"""QA Careers landing page. Uses config for URL. Click 'See all QA jobs' to go to Lever open positions."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config_loader import get_qa_careers_url


class CareersPage(BasePage):
    """QA careers landing (URL from config). Click 'See all QA jobs' to open Lever job listing."""

    LOCATOR_SEE_ALL_QA_JOBS = (By.LINK_TEXT, "See all QA jobs")

    def __init__(self, driver):
        super().__init__(driver, base_url=get_qa_careers_url())

    def load(self):
        """Open QA careers page (qa_careers_url from config.json)."""
        self.driver.get(self.base_url)

    def click_see_all_qa_jobs(self):
        """Click 'See all QA jobs'; navigates to open positions. Scroll into view + JS click to avoid overlay (e.g. cookie bar) intercepting."""
        self.wait_for_visible(self.LOCATOR_SEE_ALL_QA_JOBS)
        self.scroll_into_view(self.LOCATOR_SEE_ALL_QA_JOBS)
        self.click_js(self.LOCATOR_SEE_ALL_QA_JOBS)
