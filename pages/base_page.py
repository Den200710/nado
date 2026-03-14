from playwright.sync_api import Page
from playwright.sync_api import Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until='networkidle')

    def reload(self, url: str):
        self.page.reload(wait_until='domcontentloaded')

    def check_after(self, element: Locator, should_have_after: bool) -> None:
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

