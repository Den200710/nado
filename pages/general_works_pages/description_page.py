from __future__ import annotations

from playwright.sync_api import Page
from components.create_work.work_data_component import WorkDataComponent
from components.created_work.dangerous_data_component import DangerousDataComponent
from pages.base_page import BasePage
from components.navigation.work_page_tabs_component import WorkPageTabsComponent

class DescriptionPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.work_tabs = WorkPageTabsComponent(page)
        self.work_data_component = WorkDataComponent(page)
        self.dangerous_data = DangerousDataComponent(page)

    def verify_dangerous_data_matches_created(self, created_data: dict) -> None:
        self._data_fields = [
            ('name', 'name', 'Name', False),
            ('plot', 'plot', 'Plot', True),
            ('work_kind', 'work_kind', 'Work kind', False),
            ('work_plan', 'work_plan', 'Work_plan', True),
            ('nightly_work', 'nightly_work', 'Nightly_work', False),
            ('temperature_measurement', 'temperature_measurement', 'Temperature_measurement', False),
            ('order', 'order', 'Order', True),
            # ('specificity', 'specificity', 'Work_specificity', False),
        ]
        for actual_key, expected_key, field_name, need_normalize in self._data_fields:
            self.verify_field(
                self.dangerous_data.get_value(actual_key),
                created_data.get(expected_key, ''),
                field_name,
                need_normalize
            )


