from playwright.sync_api import Page

from components.base_component import BaseComponent


class ResponsibleEmployeeComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Определяем локаторы в словаре
        self._locators = {
            'executor': page.locator("(//a/div[contains(@class,'formatters-common_content')])[3]"),
            'admitter': page.locator("(//a/div[contains(@class,'formatters-common_content')])[5]"),
            'permit_issuer': page.locator("(//a/div[contains(@class,'formatters-common_content')])[6]"),
            'representative_gss': page.locator("(//a/div[contains(@class,'formatters-common_content')])[8]"),
            'shift_supervisor': page.locator("(//a/div[contains(@class,'formatters-common_content')])[10]")
            }


    def get_value(self, field_name: str) -> str:
        """Получить значение поля по имени"""
        locator = self._locators.get(field_name)
        if not locator:
            raise ValueError(f"Unknown field: {field_name}")

        return locator.text_content().strip()