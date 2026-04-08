from playwright.sync_api import Page

from components.base_component import BaseComponent


class DangerousDataComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Определяем локаторы в словаре
        self._locators = {
            'block_title': page.locator("//div[contains(@class,'block_title')][text()='Данные опасной работы']"),
            'status': page.locator("//div/span[contains(@class,'danger-work-status')]"),
            'name': page.locator("(//div[contains(@class,'parameters-card_item_value')]/span)[2]"),
            'external_number': page.locator("(//div[contains(@class,'parameters-card_item_value')])[6]"),
            'kind': page.locator("(//div[contains(@class,'parameters-card_item_value')]/span)[4]"),
            'special_plan': page.locator("(//div[contains(@class,'parameters-card_item_value')])[10]"),
            'nightly_work': page.locator("(//div[contains(@class,'parameters-card_item_value')])[12]"),
            'temperature_measurement': page.locator("(//div[contains(@class,'parameters-card_item_value')])[14]"),
            'plot': page.locator("(//div[contains(@class,'parameters-card_item_value')])[16]"),
            'order': page.locator("(//div[contains(@class,'parameters-card_item_value')])[18]"),
            'author': page.locator("((//div[contains(@class,'parameters-card_item_value')])[3])//a"),
            'organization_team': page.locator("(//div[contains(@class,'parameters-card_item')]/span)[3]"),
            'work_type': page.locator(
                "//div[contains(@class,'parameters-card_item_value')]//span[contains(text(),'работы')]"),
            'performing_team': page.locator("//div[contains(@class,'parameters-card_item')]/a"),
            'work_specificity': page.locator("(//div[contains(@class,'parameters-card_item_value')])[11]"),
            'holiday_work': page.locator("(//div[contains(@class,'parameters-card_item_value')])[13]"),
            'character_work': page.locator("(//div[contains(@class,'parameters-card_item_value')])[15]"),
            'count_prolongation_days': page.locator("(//div[contains(@class,'parameters-card_item_value')])[17]"),
        }

    def get_value(self, field_name: str) -> str:
        """Получить значение поля по имени"""
        locator = self._locators.get(field_name)
        if not locator:
            raise ValueError(f"Unknown field: {field_name}")
        return locator.text_content().strip()



