from playwright.sync_api import Page

from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from components.toolbar.toolbar_component import ToolbarComponent
from components.toolbar.toolbar_title_page_component import ToolbarTitlePageComponent
from components.toolbar.toolbar_print_menu_component import ToolbarPrintMenuComponent


class AllWorksPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.toolbar = ToolbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.check_title_page = ToolbarTitlePageComponent(page)
        self.toolbar_print = ToolbarPrintMenuComponent
