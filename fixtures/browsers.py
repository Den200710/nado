import re
from typing import Any, Generator

import pytest
import requests
from playwright.sync_api import Playwright, Page


@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page, Any, None]:
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


@pytest.fixture
def auto_cleanup_work():
    """Автоматически удаляет работу после теста"""
    work_items = []

    def register(page_obj):
        """Регистрирует работу для удаления"""
        match = re.search(r'/(\w+-work)/(\d+)', page_obj.url)
        if match:
            work_type = match.group(1)
            work_id = int(match.group(2))
            work_items.append({'type': work_type, 'id': work_id, 'page': page_obj})
            print(f"✅ Registered: {work_type}/{work_id}")
        else:
            print(f"❌ No work ID found in URL: {page_obj.url}")

    yield register

    for item in work_items:
        try:
            url = f"http://nuzhno2.lan/backend-main/{item['type']}/{item['id']}"

            response = item['page'].request.delete(
                url,
                headers={
                    "Accept": "*/*",
                    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Origin": "http://nuzhno2.lan",
                    "Pragma": "no-cache",
                    "Referer": f"http://nuzhno2.lan/nado/{item['type']}/{item['id']}/details"
                }
            )
            print(f" Cleaned up {item['type']}/{item['id']}: {response.status}")
            if response.status == 200:
                print(f"✅ Successfully soft-deleted work {item['id']}")
            else:
                print(f"⚠️ Unexpected status: {response.status}")
        except Exception as e:
            print(f"❌ Cleanup failed: {e}")




