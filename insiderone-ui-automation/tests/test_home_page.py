"""Tests for Insider One home page (pages/home_page.py)."""
import pytest

from pages.home_page import HomePage


class TestHomePage:
    """Verify home page opens and all main blocks load."""

    def test_navigate_to_home_page(self, driver):
        """Navigate to home page and assert it opened."""
        home = HomePage(driver)
        home.load()
        assert home.is_opened(), (
            f"Expected current URL to be {home.base_url!r}, got {driver.current_url!r}"
        )

    def test_main_blocks_loaded(self, driver):
        """Navigate to home page and assert all main blocks are loaded."""
        home = HomePage(driver)
        home.load()
        assert home.is_opened(), "Home page did not open before checking blocks"
        home.wait_for_main_blocks_loaded()
