from playwright.sync_api import Page

from components.base_component import BaseComponent


class ApproversComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)


        self.supervisor_team_label = page.locator(
            "//label[text()='Руководитель объекта (руководитель подразделения - выдающий)']")
        self.supervisor_team_field = page.locator("(//input[@id='employee_id'])[1]")
        self.supervisor_team_position = page.locator("(//div[contains(@class,'approver-item_position')]//span)[1]")
        self.labor_protection_label = page.locator("//label[text()='Служба ОТ']")
        self.labor_protection_field = page.locator("(//input[@id='employee_id'])[2]")
        self.labor_protection_position = page.locator("(//div[contains(@class,'approver-item_position')]//span)[2]")
        self.department_pkpb_label = page.locator("//label[text()='Отдел ПКПБ']")
        self.department_pkpb_field = page.locator("(//input[@id='employee_id'])[3]")
        self.department_pkpb_position = page.locator("(//div[contains(@class,'approver-item_position')]//span)[3]")
        self.representative_gss_label = page.locator("//label[text()='Представитель ГСС (ПАСФ)']")
        self.representative_gss_field = page.locator("(//input[@id='employee_id'])[4]")
        self.representative_gss_position = page.locator("(//div[contains(@class,'approver-item_position')]//span)[4]")
        self.approver_label = page.locator("//label[text()='Утверждающий']")
        self.approver_field = page.locator("(//input[@id='employee_id'])[5]")
        self.approver_position = page.locator("(//div[contains(@class,'approver-item_position')]//span)[5]")


    def click_labor_protection_field(self):
        self.labor_protection_field.click()

    def click_department_pkpb_field(self):
        self.department_pkpb_field.click()

    def click_representative_gss_field(self):
        self.representative_gss_field.click()

    def click_approver_field(self):
        self.approver_field.click()

    def check_visible_supervisor_team_position(self):
        self.supervisor_team_position.is_visible()

    def check_visible_labor_protection_position(self):
        self.labor_protection_position.is_visible()

    def check_visible_department_pkpb_position(self):
        self.department_pkpb_position.is_visible()

    def check_visible_representative_gss_position(self):
        self.representative_gss_position.is_visible()

    def check_visible_approver_position(self):
        self.approver_position.is_visible()