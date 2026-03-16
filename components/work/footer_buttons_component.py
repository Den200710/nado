from playwright.sync_api import Page

from components.base_component import BaseComponent


class FooterButtonsComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.height_cancel_button = page.locator("(//button[text()='Отмена'])[1]")
        self.height_save_button = page.locator("(//button[text()='Сохранить'])[1]")
        self.low_cancel_button = page.locator("(//button[text()='Отмена'])[2]")
        self.low_save_button = page.locator("(//button[text()='Сохранить'])[2]")

    def click_height_cancel(self):
        self.height_cancel_button.click()

    def click_height_save(self):
        self.height_save_button.click()

    def click_low_cancel(self):
        self.low_cancel_button.click()

    def click_low_save(self):
        self.low_save_button.click()
