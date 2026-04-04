import pytest
from playwright.sync_api import Page

from pages.authentication.login_page import LoginPage
from pages.gas_works.all_works_page import AllWorksPage
from pages.gas_works.create_gas_work_page import CreateGasWorkPage
from pages.gas_works.current_works_page import CurrentWorksPage
from pages.gas_works.to_approval_works_page import ToApprovalWorksPage
from pages.monitoring.operational_plan_page import OperationalPlanPage
from components.toolbar.toolbar_component import ToolbarComponent
from pages.general_works_pages.description_page import DescriptionPage

@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def operational_plan_page(initialize_browser_without_state: Page) -> OperationalPlanPage:
    return OperationalPlanPage(page=initialize_browser_without_state)

@pytest.fixture
def to_approval_page(initialize_browser_without_state: Page) -> ToApprovalWorksPage:
    return ToApprovalWorksPage(page=initialize_browser_without_state)

@pytest.fixture
def current_works_page(initialize_browser_without_state: Page) -> CurrentWorksPage:
    return CurrentWorksPage(page=initialize_browser_without_state)

@pytest.fixture
def all_works_page(initialize_browser_without_state: Page) -> AllWorksPage:
    return AllWorksPage(page=initialize_browser_without_state)

@pytest.fixture
def create_gas_work_page(initialize_browser_without_state: Page) -> CreateGasWorkPage:
    return CreateGasWorkPage(page=initialize_browser_without_state)

@pytest.fixture
def toolbar_component(initialize_browser_without_state: Page) -> ToolbarComponent:
    return ToolbarComponent(page=initialize_browser_without_state)

@pytest.fixture
def description_page(initialize_browser_without_state: Page) -> DescriptionPage:
    return DescriptionPage(page=initialize_browser_without_state)
