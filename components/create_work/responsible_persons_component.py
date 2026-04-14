from playwright.sync_api import Page
from components.base_component import BaseComponent
from pages.base_page import BasePage


class ResponsiblePersonsComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.base_page = BasePage(page)
        self.identifier = identifier

        self.responsible_person_field = page.locator(f"//input[@id='approver_{identifier}_id']")
        self.responsible_person_label = page.locator(f"//label[@id='approver_{identifier}_id-control-label']")
        self.select_first_responsible_in_list = page.locator("(//div[contains(@class,'employee-fio')])[1]")

    def click_select_responsible(self) -> None:
        self.responsible_person_field.click()

    def get_value(self) -> str:
        return self.responsible_person_field.input_value()

    def click_responsible_person_field(self) -> None:
        self.responsible_person_field.click()

    def click_select_first_responsible_in_list(self) -> None:
        self.select_first_responsible_in_list.click()
