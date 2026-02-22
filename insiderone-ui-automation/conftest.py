"""
Project-wide pytest config (conftest at root so driver, pages, utils import without path hacks).
Browser from CLI (--browser), env (BROWSER), or config. Screenshot on test failure.
"""
import os
import pytest

from driver.driver_manager import DriverManager
from utils.config_loader import get_browser
from utils.screenshot_util import ScreenshotUtil


def pytest_addoption(parser):
    """Add --browser option: pytest --browser=chrome or pytest --browser=firefox"""
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser to run tests: chrome or firefox (default: from BROWSER env or config)",
    )


def _get_browser(request):
    """Priority: CLI --browser > env BROWSER > config.json. Normalized to lowercase."""
    raw = request.config.getoption("--browser", default=None) or os.environ.get("BROWSER") or get_browser()
    return (raw or "").strip().lower()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store test result so driver fixture can check if test failed (for screenshot)."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function")
def driver(request):
    """Create WebDriver for the browser chosen via --browser, BROWSER env, or config."""
    browser = _get_browser(request)
    manager = DriverManager(browser=browser)
    d = manager.start_driver()
    d.maximize_window()

    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_util = ScreenshotUtil(d, screenshot_dir)

    yield d

    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        screenshot_util.capture_screenshot(request.node.name)

    manager.quit_driver()
