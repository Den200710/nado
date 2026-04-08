from __future__ import annotations

from playwright.sync_api import Page
from components.create_work.work_data_component import WorkDataComponent
from components.created_work.dangerous_data_component import DangerousDataComponent
from pages.base_page import BasePage
from components.navigation.work_page_tabs_component import WorkPageTabsComponent


def normalize_value(value: str) -> str:
    """Нормализует значение для сравнения"""
    if not value:
        return ''
    cleaned = value.strip()
    return '' if cleaned in ['-', '—'] else cleaned


class DescriptionPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.work_tabs = WorkPageTabsComponent(page)
        self.work_data_component = WorkDataComponent(page)
        self.dangerous_data = DangerousDataComponent(page)

    def verify_dangerous_data_matches_created(self, created_data: dict) -> None:
        actual_name = self.dangerous_data.get_value('name')
        assert actual_name == created_data.get('name', ''), \
            f"Name mismatch: expected '{created_data.get('name')}', got '{actual_name}'"

        actual_plot = normalize_value(self.dangerous_data.get_value('plot'))
        expected_plot = normalize_value(created_data.get('plot', ''))

        assert actual_plot == expected_plot, \
            f"Plot mismatch: expected '{created_data.get('plot')}', got '{self.dangerous_data.get_value('plot')}'"


