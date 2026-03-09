from playwright.sync_api import Page, expect

from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class OperationalPlanPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)

        self.main_title = page.locator("//div[contains(@class,'view-header_titles')]")

    def check_visible_main_title(self):
        expect(self.main_title).to_have_text('Мониторинг')
