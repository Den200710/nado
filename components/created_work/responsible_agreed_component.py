from playwright.sync_api import Page

from components.base_component import BaseComponent


class ResponsibleAgreedComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._locators_person = {
            'supervisor_team': page.locator(
                "(//div[contains(@class,'work-details-description_approver_info')]/div[2])[1]/div"),
            'labor_protection': page.locator(
                "(//div[contains(@class,'work-details-description_approver_info')]/div[2])[2]/div"),
            'department_pkpb': page.locator(
                "(//div[contains(@class,'work-details-description_approver_info')]/div[2])[3]/div"),
            'representative_gss': page.locator(
                "(//div[contains(@class,'work-details-description_approver_info')]/div[2])[4]/div"),
            'approver': page.locator(
                "(//div[contains(@class,'work-details-description_approver_info')]/div[2])[5]/div")
            }

        self._locators_position = {
            'supervisor_team_position': page.locator(
                "(//div[contains(@class,'work-details-description_approver_info')]/div/b)[2]"),
            'labor_protection_position': page.locator(
                "(//div[contains(@class,'work-details-description_approver_info')]/div/b)[4]"),
            'department_pkpb_position': page.locator(
                "(//div[contains(@class,'work-details-description_approver_info')]/div/b)[6]"),
            'representative_gss_position': page.locator(
                "(//div[contains(@class,'work-details-description_approver_info')]/div/b)[8]"),
            'approver_position': page.locator("(//div[contains(@class,'work-details-description_approver_info')]/div/b)[10]")
            }

    def get_value_person(self, field_name: str) -> str:
        """Получить значение поля по имени"""
        locator = self._locators_person.get(field_name)
        if not locator:
            raise ValueError(f"Unknown field: {field_name}")

        return locator.text_content().strip()

    def get_value_position(self, field_name: str) -> str:
        """Получить значение поля по имени"""
        locator = self._locators_position.get(field_name)
        if not locator:
            raise ValueError(f"Unknown field: {field_name}")

        return locator.text_content().strip()


