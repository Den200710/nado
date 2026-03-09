from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.locator("//input[@id='username']")
        self.password_input = page.locator("//input[@id='password']")
        self.login_button = page.locator("//button[@type='submit']")

    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_login_button(self):
        self.login_button.click()
        

