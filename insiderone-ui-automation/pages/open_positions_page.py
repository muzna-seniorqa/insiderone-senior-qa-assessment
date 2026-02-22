"""Open positions on Insider One careers page, 'See all QA jobs'."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class OpenPositionsPage(BasePage):
    """Open positions section (Browse Open Positions). Reached from careers → See all QA jobs → scroll into view."""

    LOCATOR_CAREER_POSITION_LIST = (By.ID, "career-position-list")
    LOCATOR_FILTER_LOCATION = (By.ID, "filter-by-location")
    LOCATOR_FILTER_DEPARTMENT = (By.ID, "filter-by-department")
    LOCATOR_JOB_CARDS = (By.CSS_SELECTOR, "#jobs-list .position-list-item")
    VIEW_ROLE_IN_CARD = (By.XPATH, ".//a[contains(text(),'View Role') and contains(@href,'lever')]")

    def __init__(self, driver):
        super().__init__(driver, base_url=None)

    def scroll_to_browse_open_positions(self):
        """Scroll so 'Browse Open Positions' section (and filters) is in view."""
        self.scroll_into_view(self.LOCATOR_CAREER_POSITION_LIST)

    def wait_for_locations_loaded(self, location_value, timeout=None):
        """Wait until the Location dropdown has the given option. Uses DEFAULT_TIMEOUT (60s) if timeout not passed."""
        self.wait_for_visible(self.LOCATOR_FILTER_LOCATION, timeout=timeout)
        self.wait_for_element(
            (By.XPATH, f"//select[@id='filter-by-location']/option[normalize-space(text())='{location_value}']"),
            timeout=timeout,
        )

    def wait_for_department_loaded(self, department_value, timeout=None):
        """Wait until the Department dropdown has the given option. Uses DEFAULT_TIMEOUT (60s) if timeout not passed."""
        self.wait_for_visible(self.LOCATOR_FILTER_DEPARTMENT, timeout=timeout)
        self.wait_for_element(
            (By.XPATH, f"//select[@id='filter-by-department']/option[normalize-space(text())='{department_value}']"),
            timeout=timeout,
        )

    def select_location(self, location):
        """Select Location by visible text (e.g. 'Istanbul, Turkiye')."""
        el = self.wait_for_clickable(self.LOCATOR_FILTER_LOCATION)
        Select(el).select_by_visible_text(location)

    def select_department(self, department):
        """Select Department by visible text (e.g. 'Quality Assurance')."""
        el = self.wait_for_clickable(self.LOCATOR_FILTER_DEPARTMENT)
        Select(el).select_by_visible_text(department)

    def wait_for_job_list_updated(self, location_in_card):
        """Wait until job list has updated after filter (at least one card contains the selected location)."""
        def card_with_location(driver):
            cards = driver.find_elements(*self.LOCATOR_JOB_CARDS)
            return any(location_in_card in card.text for card in cards)
        self.wait.until(card_with_location)

    def apply_filters(self, location, department):
        """Scroll to section, wait for dropdowns to load, select filters, then wait for job list to update."""
        self.scroll_to_browse_open_positions()
        self.wait_for_locations_loaded(location)
        self.wait_for_department_loaded(department)
        self.select_location(location)
        self.select_department(department)
        self.wait_for_job_list_updated(location)

    def get_job_cards(self):
        """Return list of job card WebElements. Uses base find_elements (wait then return all)."""
        try:
            return self.find_elements(self.LOCATOR_JOB_CARDS)
        except Exception:
            return []

    def click_view_role_on_matching_job(self, position_contains, department_contains, location_contains):
        """Click View Role on the first job card that matches title, department, and location."""
        cards = self.get_job_cards()
        for card in cards:
            text = card.text
            if (
                position_contains in text
                and department_contains in text
                and location_contains in text
            ):
                self.find_element_within(card, self.VIEW_ROLE_IN_CARD).click()
                return
        raise AssertionError(
            f"No job card matched (title contains '{position_contains}', "
            f"department '{department_contains}', location '{location_contains}')"
        )
