from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class ToolbarTitlePageComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = page.locator("(//div[contains(@class,'view-header_title')])[2]")

    def check_visible_page_title(self, title):
        expect(self.page_title).to_be_visible()
        expect(self.page_title).to_have_text(title)