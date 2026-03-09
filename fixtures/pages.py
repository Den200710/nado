import pytest
from playwright.sync_api import Page

from pages.authentication.login_page import LoginPage
from pages.gas_works.to_approval_works_page import ToApprovalWorksPage
from pages.monitoring.operational_plan_page import OperationalPlanPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def operational_plan_page(initialize_browser_without_state: Page) -> OperationalPlanPage:
    return OperationalPlanPage(page=initialize_browser_without_state)

@pytest.fixture
def to_approval_page(initialize_browser_without_state: Page) -> ToApprovalWorksPage:
    return ToApprovalWorksPage(page=initialize_browser_without_state)

