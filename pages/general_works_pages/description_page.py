from playwright.sync_api import Page

from pages.base_page import BasePage
from components.navigation.work_page_tabs_component import WorkPageTabsComponent


class DescriptionPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.work_tabs = WorkPageTabsComponent(page)


