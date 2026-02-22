"""
E2E: QA jobs flow. All filter and assertion values come from data/filter_data.yaml (edit YAML only).
1. Go to QA careers URL (config), click "See all QA jobs"
2. Scroll to Browse Open Positions, wait for locations, select Location & Department from data
3. Assert job list; each job contains expected Position / Department / Location from data
4. Click "View Role" on a matching job, assert redirect to Lever (lever_domain from data)

Browser: --browser=chrome|firefox, or BROWSER env, or config.json "browser".
"""
import pytest

from pages.careers_page import CareersPage
from pages.open_positions_page import OpenPositionsPage
from pages.job_page import JobPage
from utils.data_reader import get_data


class TestQAJobsFlow:

    def setup_test_data(self):
        """Load test data once for all tests (same pattern as get_data('Data/test_data.yaml'))."""
        self.test_data = get_data("data/filter_data.yaml")
        self.filter_data = self.test_data["filter"]
        self.location = self.filter_data["location"]
        self.department = self.filter_data["department"]
        self.position_contains = self.test_data["expected_position_contains"]
        self.lever_domain = self.test_data["lever_domain"]

    def test_qa_jobs_flow_e2e(self, driver):
        self.setup_test_data()

        # --- 1. Go to QA careers, click "See all QA jobs" ---
        careers_page = CareersPage(driver)
        careers_page.load()
        careers_page.click_see_all_qa_jobs()

        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])

        # --- 2. Open positions: apply filters from data ---
        open_positions = OpenPositionsPage(driver)
        open_positions.apply_filters(self.location, self.department)

        # --- 3. Assert all jobs: Position contains "Quality Assurance", Department "Quality Assurance", Location "Istanbul, Turkiye" ---
        job_cards = open_positions.get_job_cards()
        assert len(job_cards) > 0, "No jobs in list after filtering by Location and Department"

        for i, card in enumerate(job_cards):
            card_text = card.text
            assert self.position_contains in card_text, (
                f"Job {i + 1}: Position should contain '{self.position_contains}', got: {card_text[:200]}"
            )
            assert self.department in card_text, (
                f"Job {i + 1}: Department should contain '{self.department}', got: {card_text[:200]}"
            )
            assert self.location in card_text, (
                f"Job {i + 1}: Location should contain '{self.location}', got: {card_text[:200]}"
            )

        # --- 4. Click View Role on the first card that matches title, department, location -> redirect to Lever ---
        open_positions.click_view_role_on_matching_job(
            self.position_contains, self.department, self.location
        )

        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])

        job_page = JobPage(driver)
        assert job_page.wait_for_lever_page(self.lever_domain)
