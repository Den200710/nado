from playwright.sync_api import Page
from components.base_component import BaseComponent
from pages.base_page import BasePage


class ResponsiblePersonsComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.base_page = BasePage(page)
        self.identifier = identifier

        self.approver_person_field = page.locator(f"//input[@id='approver_{identifier}_id']")
        self.approver_person_label = page.locator(f"//label[@id='approver_{identifier}_id-control-label']")

    def click_select_responsible(self) -> None:
        self.approver_person_field.click()

    def clear(self) -> None:
        self.approver_person_field.clear()

    def get_value(self) -> str:
        return self.approver_person_field.input_value()

    def check_required_field(self, should_have_after: bool) -> None:
        self.base_page.check_after(self.approver_person_label, should_have_after)