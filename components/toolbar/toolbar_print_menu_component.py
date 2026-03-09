from playwright.sync_api import Page

from components.base_component import BaseComponent


class ToolbarPrintMenuComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.print_dropdown_item = page.locator(f"//li[text()='{identifier}']")

    def select_print_dropdown_item_click(self):
        self.print_dropdown_item.click()
