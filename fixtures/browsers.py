import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_without_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("http://nuzhno2.lan/")
    email_input = page.locator("//input[@id='username']")
    email_input.fill('test17@test.test')

    password_input = page.locator("//input[@id='password']")
    password_input.fill('123654')

    login_button = page.locator("//button[@type='submit']")
    login_button.click()
    page.wait_for_url("**/operational_plan")
    yield page
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://nuzhno2.lan/")

    email_input = page.locator("//input[@id='username']")
    email_input.fill('test17@test.test')

    password_input = page.locator("//input[@id='password']")
    password_input.fill('123654')

    login_button = page.locator("//button[@type='submit']")
    login_button.click()
    page.wait_for_url("**/operational_plan")
    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()