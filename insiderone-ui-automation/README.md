# Insider One QA Automation

E2E tests for the QA careers flow. Edit `data/filter_data.yaml` for filters and assertions; edit `config/config.json` for URLs and default browser.

**Stack:** **Python** · **pytest** (test runner) · **Selenium** (browser automation)  
**Design pattern:** **Page Object Model (POM)** — each screen has a page class with locators and actions; tests orchestrate the flow.  
**Data-driven:** Test data (filters, expected text, Lever domain) is read from `data/filter_data.yaml`, so you change behaviour by editing the YAML instead of the test code.

---

## Run tests

```bash
# from project root, with venv activated
pytest tests/ -v
```

Use `--browser=chrome` or `--browser=firefox` to override the default browser (see [Browser selection](#browser-selection)).

---

## ChromeDriver (Chrome 145+)

Chrome updates often ship before Selenium’s default driver manager supports them. **Chrome 145** is one such case, so ChromeDriver is expected to be **installed manually** and on your **PATH**.

- Download the matching [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) for your Chrome version (e.g. 145.x).
- Put the executable on PATH (or in a directory already on PATH) so `webdriver.Chrome()` can find it.

Firefox uses GeckoDriver; ensure it’s on PATH when using `--browser=firefox`.

---

## Browser selection

You can choose the browser in **three ways** (highest priority first):

| Priority | How | Example |
|----------|-----|--------|
| 1 | CLI | `pytest tests/ --browser=firefox` |
| 2 | Env variable (in terminal) | In the same terminal, set `BROWSER` then run pytest. Windows CMD: `set BROWSER=firefox`. PowerShell: `$env:BROWSER="firefox"`. Linux/macOS: `export BROWSER=firefox`. Then: `pytest tests/` |
| 3 | Config file | Set `"browser": "chrome"` or `"firefox"` in `config/config.json` (default) |

So: **CLI overrides env variable, env variable overrides config file.** There is no separate “environment” file in the project — option 2 is the OS/shell environment.

---

## Why JavaScript click on the careers page?

The careers page shows a **cookie/consent overlay**. A normal Selenium click can hit the overlay instead of the “See all QA jobs” link. The test uses a **JavaScript click** (`click_js` in `BasePage`) so the click is delivered to the link even when the overlay is present. This is used only where the overlay would otherwise block the action (e.g. Careers page “See all QA jobs”).

---

## Timeouts (60 seconds default)

Loading **Location** and **Department** dropdowns on the open positions page can be slow. To avoid flaky failures, **explicit waits use a 60-second default** (`BasePage.DEFAULT_TIMEOUT`). You can override per call where needed (e.g. `wait_for_element(locator, timeout=30)`).

---

## Page objects (why three pages?)

The E2E flow in `tests/test_insider_qa.py` uses **three page classes** in order: **CareersPage** → **OpenPositionsPage** → **JobPage**. Each class matches a distinct screen/URL:

- **CareersPage** — QA careers landing; loads URL and clicks “See all QA jobs”.
- **OpenPositionsPage** — Lever open positions; applies Location/Department filters, asserts job list, clicks “View Role”.
- **JobPage** — Lever application (new tab); waits for URL to contain the Lever domain.

One class per screen keeps locators and actions in one place and makes the test a simple sequence of page actions. The test does not duplicate selectors or wait logic; it just orchestrates the flow across these pages.

---

## Key utilities

- **config_loader** (`utils/config_loader.py`) — Loads `config/config.json`; provides `get_qa_careers_url()`, `get_browser()`, etc. Used by pages and driver so URLs and default browser live in config.
- **data_reader** (`utils/data_reader.py`) — Loads YAML (e.g. `data/filter_data.yaml`). Used by the test to get filters, expected text, and Lever domain without hardcoding.
- **screenshot_util** (`utils/screenshot_util.py`) — Captures a screenshot on test failure. Wired in `conftest.py`; images are saved under `screenshots/`.

---

## Other details

- **Test data**: Filters (location, department), expected text, and Lever domain come from `data/filter_data.yaml`. Change that file to adjust test criteria.
- **Config**: `config/config.json` holds `base_url`, `qa_careers_url`, and default `browser`.

---

## Setup

```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

Then install ChromeDriver (and GeckoDriver if using Firefox) as described above and run `pytest tests/ -v`.
