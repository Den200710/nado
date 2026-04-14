from playwright.sync_api import Page

from components.base_component import BaseComponent


class ApproversComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)


        self.supervisor_team_label = page.locator(
            "//label[text()='Руководитель объекта (руководитель подразделения - выдающий)']")
        self.labor_protection_label = page.locator("//label[text()='Служба ОТ']")
        self.department_pkpb_label = page.locator("//label[text()='Отдел ПКПБ']")
        self.representative_gss_label = page.locator("//label[text()='Представитель ГСС (ПАСФ)']")
        self.approver_label = page.locator("//label[text()='Утверждающий']")

        self._locators_person = {
            'supervisor_team': page.locator("(//input[@id='employee_id'])[1]"),
            'labor_protection': page.locator("(//input[@id='employee_id'])[2]"),
            'department_pkpb': page.locator("(//input[@id='employee_id'])[3]"),
            'representative_gss': page.locator("(//input[@id='employee_id'])[4]"),
            'approver': page.locator("(//input[@id='employee_id'])[5]")
            }
        self._locators_position = {
            'supervisor_team_position': page.locator("(//div[contains(@class,'approver-item_position')]//span)[1]"),
            'labor_protection_position': page.locator("(//div[contains(@class,'approver-item_position')]//span)[2]"),
            'department_pkpb_position': page.locator("(//div[contains(@class,'approver-item_position')]//span)[3]"),
            'representative_gss_position': page.locator("(//div[contains(@class,'approver-item_position')]//span)[4]"),
            'approver_position': page.locator("(//div[contains(@class,'approver-item_position')]//span)[5]")
            }


    def click_approvers(self, approver: str) -> None:
        """Кликнуть на поле"""
        locator = self._locators_person.get(approver)
        locator.click()

    def check_visible_approvers(self, approver: str) -> None:
        """Проверить, что поле заполнилось"""
        locator = self._locators_person.get(approver)
        locator.is_visible()

    def get_approver_value(self, field_name: str) -> str:
        """Получить значение поля по имени (работает с любыми элементами)"""
        locator = self._locators_person.get(field_name)
        if not locator:
            raise KeyError(f"Field '{field_name}' not found")
        value = None
        try:
            value = locator.input_value()
        except Exception:
            pass
        if value is None:
            value = locator.get_attribute("value")
        if not value:
            value = locator.text_content()
        return value.strip() if value else ''

    def get_approver_position_value(self, field_name: str) -> str:
        """Получить значение поля по имени (работает с любыми элементами)"""
        locator = self._locators_position.get(field_name)
        if not locator:
            raise KeyError(f"Field '{field_name}' not found")
        value = None
        try:
            value = locator.input_value()
        except Exception:
            pass
        if value is None:
            value = locator.get_attribute("value")
        if not value:
            value = locator.text_content()
        return value.strip() if value else ''

    def get_all_approvers_data(self) -> dict:
        """Получить все данные"""
        return {
            'supervisor_team': self.get_approver_value('supervisor_team'),
            'labor_protection': self.get_approver_value('labor_protection'),
            'department_pkpb': self.get_approver_value('department_pkpb'),
            'representative_gss': self.get_approver_value('representative_gss'),
            'approver': self.get_approver_value('approver'),
            'supervisor_team_position': self.get_approver_position_value('supervisor_team_position'),
            'labor_protection_position': self.get_approver_position_value('labor_protection_position'),
            'department_pkpb_position': self.get_approver_position_value('department_pkpb_position'),
            'representative_gss_position': self.get_approver_position_value('representative_gss_position'),
            'approver_position': self.get_approver_position_value('approver_position'),
        }
