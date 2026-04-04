from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class ToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_from_template_button = page.locator("//span[text()='Создать из шаблона']")
        self.create_work_button = page.locator("//span[text()=' Добавить н/д']")
        self.print_dropdown_list = page.locator("//button[contains(@class,'view-header_action_menu_btn')]")
        self.update_list_button = page.locator("//button[@title='Обновить список']")
        self.filter_button = page.locator("//button[@title='Фильтры']")
        self.header_sub_title = page.locator("//div[contains(@class,'view-header_subtitle')]")
        self.on_approval_button = page.locator("//button[@title='Отправить на согласование']")

    def click_from_template_button(self):
        self.create_from_template_button.click()

    def click_create_work_button(self):
        self.create_work_button.click()

    def click_print_dropdown_list(self):
        self.print_dropdown_list.click()

    def click_update_list_button(self):
        self.update_list_button.click()

    def click_filter_button(self):
        self.filter_button.click()

    def check_visible_sub_title(self):
        expect(self.header_sub_title).to_have_text("Наряды-допуски")

    def check_visible_on_approval_button(self):
        expect(self.on_approval_button).to_be_visible(timeout=7000)
        expect(self.on_approval_button).to_be_enabled()
