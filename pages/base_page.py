from playwright.sync_api import Page
from playwright.sync_api import Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until='networkidle')

    def reload(self, url: str):
        self.page.reload(wait_until='domcontentloaded')

    def check_after(self, element: Locator):
        """
        Проверяет наличие псевдоэлемента ::after у элемента
        """
        # Используем evaluate для выполнения JavaScript на элементе
        has_after = self.page.evaluate("""
            (element) => {
                const computedStyle = window.getComputedStyle(element, '::after');
                const content = computedStyle.content;
                return content !== 'none' && content !== '' && content !== 'normal';
            }
        """, element.element_handle())

        return has_after

