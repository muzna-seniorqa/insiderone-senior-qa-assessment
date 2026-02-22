"""Base page with common actions and explicit waits (POM)."""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    DEFAULT_TIMEOUT = 60  # seconds: each explicit wait will poll until condition or 60s, whichever first

    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)
        self.base_url = base_url

    def wait_for_element(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.DEFAULT_TIMEOUT)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_for_visible(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.DEFAULT_TIMEOUT)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.DEFAULT_TIMEOUT)
        return wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def find_elements(self, locator, timeout=None):
        """Wait for at least one element (DEFAULT_TIMEOUT if not passed), then return all matching elements."""
        wait = WebDriverWait(self.driver, timeout or self.DEFAULT_TIMEOUT)
        wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def find_element_within(self, parent, locator, timeout=None):
        """Wait for a child element inside parent (DEFAULT_TIMEOUT if not passed), then return it. Use for e.g. link inside a card."""
        wait = WebDriverWait(self.driver, timeout or self.DEFAULT_TIMEOUT)

        def child_present(_):
            try:
                return parent.find_element(*locator)
            except NoSuchElementException:
                return False

        return wait.until(child_present)

    def scroll_into_view(self, locator):
        """Scroll so the element is in view (for filters/lists below the fold)."""
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click_js(self, locator):
        """Click via JavaScript (use when an overlay e.g. cookie bar intercepts normal click)."""
        element = self.wait_for_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)
