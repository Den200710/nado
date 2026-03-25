from playwright.sync_api import Page

from components.base_component import BaseComponent


class RightWindowComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.close_right_window = page.locator("//button[contains(@class,'rs-drawer-header-close')]")

    def click_close_right_window(self):
        self.close_right_window.click()


