from playwright.sync_api import Page
from pages.base_page import BasePage
from components.toolbar.toolbar_component import ToolbarComponent
from components.toolbar.toolbar_title_page_component import ToolbarTitlePageComponent
from components.toolbar.toolbar_print_menu_component import ToolbarPrintMenuComponent


class ToApprovalWorksPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.toolbar = ToolbarComponent(page)
        self.check_title_page = ToolbarTitlePageComponent(page, 'Газоопасные работы на согласовании')
        self.toolbar_print = ToolbarPrintMenuComponent


