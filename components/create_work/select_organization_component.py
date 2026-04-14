from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from pages.base_page import BasePage


class BlockSelectOrganizationComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.base_page = BasePage(page)

        self.toggle = page.locator("label:has-text('Использовать сотрудников ПО')")
        self.contracting_organization_field = page.locator("//input[@id='performing_contractor_id']")
        self.performing_team_label = page.locator("//label[@id='performing_team_id-control-label']")
        self.performing_contracting_organization_label = page.locator(
            "//label[@id='performing_contractor_id-control-label']")
        self.condition_toggle = page.locator(
            "//input[@id='performed_by_contractor']/following-sibling::span[contains(@class,'toggle-presentation')]")
        self.select_first_team = page.locator("(//div/div[contains(@class,'node_name')])[1]")

        self._input_fields = {
            'performing_team': page.locator("//input[@id='performing_team_id']")
        }

    def click_select_first_team(self):
        self.select_first_team.click()

    def click_toggle(self):
        self.toggle.is_enabled()
        self.toggle.click()

    def toggle_should_to_be_checked(self):
        expect(self.toggle).to_be_checked()

    def toggle_should_not_to_be_checked(self):
        expect(self.toggle).not_to_be_checked()

    def click_select_team(self):
        locator = self._input_fields['performing_team']
        locator.click()

    def click_select_contracting_organization(self):
        self.contracting_organization_field.click()

    def check_visible_performing_team_label(self):
        expect(self.performing_team_label).to_be_visible()
        self.base_page.check_after(self.performing_team_label, True)

    def check_visible_performing_contracting_organization_label(self):
        expect(self.performing_contracting_organization_label).to_be_visible()
        self.base_page.check_after(self.performing_contracting_organization_label, True)

    def get_field_value(self, field_name: str) -> str:
        """Получить значение поля по имени"""
        locator = self._input_fields.get(field_name)
        if not locator:
            raise KeyError(f"Field '{field_name}' not found")
        try:
            value = locator.input_value()
        except Exception:
            value = locator.get_attribute("value")
            if not value:
                value = locator.text_content()

        return value.strip() if value else ''

    def get_toggle_state(self, toggle_name: str) -> bool:
        """Получить состояние переключателя"""
        locator = self._toggles.get(toggle_name)
        if not locator:
            raise KeyError(f"Toggle '{toggle_name}' not found")
        return locator.is_checked()

    def get_all_work_data(self) -> dict:
        """Получить все данные"""
        return {
            'performing_team': self.get_field_value('performing_team')
        }

