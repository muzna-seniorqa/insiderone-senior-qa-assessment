"""Lever application / job role page (after clicking View Role). Used for URL assertions."""
from pages.base_page import BasePage


class JobPage(BasePage):
    """Represents the Lever application form page (lever.co) after 'View Role' redirect."""

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_lever_page(self, lever_domain):
        """Wait until the current URL contains lever_domain (e.g. new tab may load from about:blank)"""
        def url_contains_domain(driver):
            return lever_domain in driver.current_url

        self.wait.until(url_contains_domain)
        return True
