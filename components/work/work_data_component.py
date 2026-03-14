from playwright.sync_api import Page

from components.base_component import BaseComponent
from pages.base_page import BasePage

class WorkDataComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.base_page = BasePage(page)

        self.name_label = page.locator("//label[@id='name-control-label']")
        self.name_field = page.locator("//input[@id='name']")
        self.team_label = page.locator("//label[@id='team_id-control-label']")
        self.team_field = page.locator("//input[@id='team_id']")
        self.work_kind_label = page.locator("//label[@id='lib_work_kind_id-control-label']")
        self.work_kind_field = page.locator("//input[@id='lib_work_kind_id']")
        self.work_plan_label = page.locator("//label[@id='work_plan_id-control-label']")
        self.work_plan_field = page.locator("//input[@id='work_plan_id']")
        self.description_label = page.locator("//label[@id='work_description-control-label']")
        self.description_field = page.locator("//textarea[@id='work_description']")
        self.specificity_label = page.locator("//label[@id='lib_specificity_id-control-label']")
        self.specificity_field = page.locator("//input[@id='lib_specificity_id']")
        self.select_specificity_out = page.locator("//span[text()='Работы производятся на открытой площадке']")
        self.select_specificity_into = page.locator(
            "//span[text()='Работы производятся в замкнутом пространстве (колодец, сосуд, цистерна)']")
        self.order_name_label = page.locator("//label[@id='order_name-control-label']")
        self.order_name_field = page.locator("//textarea[@id='order_name']")
        # self.approver_certification_label = page.locator("//label[@id='approverCertifications-control-label']")
        # self.approver_certification_field = page.locator("(//div[contains(@class,'multiple-select')])[3]")
        # self.approver_certification_select_button = page.locator(
        #     "(//div[contains(@class,'multiple-select_actions')]/button)[1]")
        # self.approver_certification_clear_button = page.locator(
        #     "(//div[contains(@class,'multiple-select_actions')]/button)[2]")
        # self.approver_contracting_certification_label = page.locator(
        #     "//label[@id='approverCertificationsForContractingEmployee-control-label']")
        # self.approver_contracting_certification_field = page.locator()
        self.temperature_measurement_label = page.locator("//label[@id='measurement_required-control-label']")
        self.temperature_measurement_toggle = page.locator("//input[@id='measurement_required']")
        self.nightly_work_label = page.locator("//label[@id='nightly-control-label']")
        self.nightly_work_toggle = page.locator("//input[@id='nightly']")
        self.holiday_work_label = page.locator("//label[@id='weekend-control-label']")
        self.holiday_work_toggle = page.locator("//input[@id='weekend']")
        self.is_planned_repair_work_label = page.locator("//label[@id='is_planned_maintenance_work-control-label']")
        self.is_planned_repair_work_toggle = page.locator("//input[@id='is_planned_maintenance_work']")
        self.place_work_label = page.locator("//label[text()='Место проведения работы']")
        self.place_work_field = page.locator(
            "(//div[contains(@class,'form-control')]//div[contains(@class,'empty-data')])[1]")
        self.place_work_button = page.locator("//div[contains(@class,'view-block_header')]//span[text()='Выбрать']")
        self.plot_label = page.locator("//div[text()='Участок']")
        self.plot_field = page.locator("(//div[contains(@class,'form-control')]//textarea)[3]")



