import re
from re import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.navigation.sidebar_list_sub_item_component import SidebarListSubItemComponent


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.to_approval_works_list_sub_item = SidebarListSubItemComponent(page, 'Работы на согласовании')
        self.current_works_list_sub_item = SidebarListSubItemComponent(page, 'Мои текущие работы')
        self.all_works_list_sub_item = SidebarListSubItemComponent(page, 'Все работы')
        self.dictionaries_list_sub_item = SidebarListSubItemComponent(page, 'Справочники')
        self.templates_list_sub_item = SidebarListSubItemComponent(page, 'Шаблоны')
        self.archive_list_sub_item = SidebarListSubItemComponent(page, 'Архив')
        self.logbook_list_sub_item = SidebarListSubItemComponent(page, 'Журнал регистрации')

        self.item = page.locator(f"//div[text()='{identifier}']")

    def check_visible(self, item: str):
        expect(self.item).to_be_visible()
        expect(self.item).to_have_text(item)

    def navigate_url(self, expected_url: Pattern[str]):
        self.item.click()
        self.check_current_url(expected_url)

    def click_to_approval_works_sub_item(self):
        self.to_approval_works_list_sub_item.navigate_url(re.compile(r".*/to_approval"))

    def click_current_works_sub_item(self):
        self.current_works_list_sub_item.navigate_url(re.compile(r".*/current-works"))

    def click_all_works_sub_item(self):
        self.all_works_list_sub_item.navigate_url(re.compile(r".*/all-works"))

    def click_dictionaries_sub_item(self):
        self.dictionaries_list_sub_item.navigate_url(re.compile(r".*/dictionaries/action"))

    def click_templates_sub_item(self):
        self.templates_list_sub_item.navigate_url(re.compile(r".*/templates/list/my-team"))

    def click_archive_sub_item(self):
        self.archive_list_sub_item.navigate_url(re.compile(r".*/archive"))

    def click_logbook_sub_item(self):
        self.logbook_list_sub_item.navigate_url(re.compile(r".*/logbook"))