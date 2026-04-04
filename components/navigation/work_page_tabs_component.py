from playwright.sync_api import Page,expect

from components.base_component import BaseComponent


class WorkPageTabsComponent(BaseComponent):
    def __init__(self,page: Page):
        super().__init__(page)

        self.description = page.locator("//span[text()='Описание']")
        self.brigade = page.locator("//span[text()='Бригада']")
        self.danger_factors = page.locator("//span[text()='Опасные факторы']")
        self.safe_measures = page.locator("//span[text()='Меры безопасности']")
        self.siz = page.locator("//span[text()='СИЗ']")
        self.files = page.locator("//span[text()='Файлы']")
        self.history = page.locator("//span[text()='История изменений']")

    def clck_description_button(self):
        expect(self.description).to_be_visible()
        expect(self.description).to_be_enabled()
        self.description.click()

    def clck_brigade_button(self):
        expect(self.brigade).to_be_visible()
        expect(self.brigade).to_be_enabled()
        self.brigade.click()

    def clck_danger_factors_button(self):
        expect(self.danger_factors).to_be_visible()
        expect(self.danger_factors).to_be_enabled()
        self.danger_factors.click()

    def clck_safe_measures_button(self):
        expect(self.safe_measures).to_be_visible()
        expect(self.safe_measures).to_be_enabled()
        self.safe_measures.click()

    def clck_siz_button(self):
        expect(self.siz).to_be_visible()
        expect(self.siz).to_be_enabled()
        self.siz.click()

    def clck_files_button(self):
        expect(self.files).to_be_visible()
        expect(self.files).to_be_enabled()
        self.files.click()

    def clck_history_button(self):
        expect(self.history).to_be_visible()
        expect(self.history).to_be_enabled()
        self.history.click()