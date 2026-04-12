import re

from playwright.sync_api import Page
from playwright.sync_api import Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until='networkidle')

    def reload(self, url: str):
        self.page.reload(wait_until='domcontentloaded')

    def check_after(self, elements: Locator | list[Locator], should_have_after: bool) -> None:
        if isinstance(elements, Locator):
            elements = [elements]

        for element in elements:
            element_handle = element.element_handle()
            actual_has_after = self.page.evaluate("""
                                                  (element) => {
                                                      try {
                                                          const computedStyle = window.getComputedStyle(element, '::after');
                                                          const content = computedStyle.content;
                                                          return content !== 'none' && content !== '' && content !== 'normal';
                                                      } catch (e) {
                                                          return false;
                                                      }
                                                  }
                                                  """, element_handle)

            if actual_has_after != should_have_after:
                element_text = element.text_content() or str(element)
                raise AssertionError(
                    f"Элемент '{element_text}': ожидалось обязательное поле = {should_have_after}, "
                    f"но фактически = {actual_has_after}"
                )

    @staticmethod
    def normalize_value(value: str) -> str:
        """Нормализует значение для сравнения """
        if not value:
            return ''
        cleaned = value.strip()
        placeholders = ['-', '—']
        return '' if cleaned in placeholders else cleaned

    def verify_field(self, actual: str, expected: str, field_name: str, normalize: bool = False):
        if isinstance(expected, bool):
            expected = 'Да' if expected else 'Нет'
        if isinstance(actual, bool):
            actual = 'Да' if actual else 'Нет'
        if normalize:
            actual = self.normalize_value(actual)
            expected = self.normalize_value(expected)

        assert actual == expected, f"{field_name} mismatch: expected '{expected}', got '{actual}'"

    """Получаем id """
    def get_work_id_from_url(self) -> int | None:
        match = re.search(r'/(\d+)/details', self.page.url)
        return int(match.group(1)) if match else None


