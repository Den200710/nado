from re import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class SidebarListSubItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.sub_item = page.locator(f"//a//div[text()='{identifier}']")

    def check_visible(self, sub_item: str):
        expect(self.sub_item).to_be_visible()
        expect(self.sub_item).to_have_text(sub_item)

    def click_navigate_url(self, expected_url: Pattern[str]):
        self.sub_item.click()
        self.check_current_url(expected_url)
