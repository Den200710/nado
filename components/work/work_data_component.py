from playwright.sync_api import Page, expect

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
        self.temperature_measurement_toggle = page.locator("label:has-text('Требуется замер температуры или ГВС')")
        self.nightly_work_label = page.locator("//label[@id='nightly-control-label']")
        self.nightly_work_toggle = page.locator("label:has-text('Работа проводится в вечернее/ночное время')")
        self.holiday_work_label = page.locator("//label[@id='weekend-control-label']")
        self.holiday_work_toggle = page.locator("label:has-text('Работа проводится в выходные/праздничные дни')")
        self.is_planned_repair_work_label = page.locator("//label[@id='is_planned_maintenance_work-control-label']")
        self.is_planned_repair_work_toggle = page.locator("label:has-text('Плановые ремонтные работы')")
        self.place_work_label = page.locator("//label[text()='Место проведения работы']")
        self.place_work_field = page.locator(
            "(//div[contains(@class,'form-control')]//div[contains(@class,'empty-data')])[1]")
        self.place_work_button = page.locator("//div[contains(@class,'view-block_header')]//span[text()='Выбрать']")
        self.plot_label = page.locator("//div[text()='Участок']")
        self.plot_field = page.locator("(//div[contains(@class,'form-control')]//textarea)[3]")

    def fill_name_field(self, name: str):
        self.name_field.fill(name)

    def chek_visible_name_field(self, name: str):
        expect(self.name_field).to_have_value(name)

    def click_select_team(self):
        self.team_field.click()

    def click_work_kind_field(self):
        self.work_kind_field.click()

    def click_work_plan_field(self):
        self.work_plan_field.click()

    def fill_description_field(self, description: str):
        self.description_field.fill(description)

    def chek_visible_description_field(self, description: str):
        expect(self.description_field).to_have_value(description)

    def click_specificity_field(self):
        self.specificity_field.click()

    def click_specificity_output(self):
        self.specificity_field.click()

    def click_select_specificity_into(self):
        self.select_specificity_into.click()

    def fill_order_name_field(self, order_name: str):
        self.description_field.fill(order_name)

    def chek_visible_order_name_field(self, order_name: str):
        expect(self.description_field).to_have_value(order_name)

    def click_temperature_measurement_toggle(self):
        self.temperature_measurement_toggle.is_enabled()
        self.temperature_measurement_toggle.click()

    def temperature_measurement_toggle_should_be_enabled(self):
        expect(self.temperature_measurement_toggle).to_be_checked()

    def temperature_measurement_toggle_should_be_disabled(self):
        expect(self.temperature_measurement_toggle).not_to_be_checked()

    def click_nightly_work_toggle(self):
        self.nightly_work_toggle.is_enabled()
        self.nightly_work_toggle.click()

    def nightly_work_toggle_should_be_enabled(self):
        expect(self.nightly_work_toggle).to_be_checked()

    def nightly_work_toggle_should_be_disabled(self):
        expect(self.nightly_work_toggle).not_to_be_checked()

    def click_holiday_work_toggle(self):
        self.holiday_work_toggle.is_enabled()
        self.holiday_work_toggle.click()

    def holiday_work_toggle_should_be_enabled(self):
        expect(self.holiday_work_toggle).to_be_checked()

    def holiday_work_toggle_should_be_disabled(self):
        expect(self.holiday_work_toggle).not_to_be_checked()

    def click_is_planned_repair_work_toggle(self):
        self.is_planned_repair_work_toggle.is_enabled()
        self.is_planned_repair_work_toggle.click()

    def is_planned_repair_work_toggle_should_be_enabled(self):
        expect(self.is_planned_repair_work_toggle).to_be_checked()

    def is_planned_repair_work_toggle_should_be_disabled(self):
        expect(self.is_planned_repair_work_toggle).not_to_be_checked()

    def click_place_work_button(self):
        self.place_work_button.click()

    def chek_visible_place_work_field(self):
        expect(self.description_field).to_have_value()

    def fill_plot_field_field(self, plot_field: str):
        self.description_field.fill(plot_field)

    def chek_visible_plot_field_field(self, plot_field: str):
        expect(self.description_field).to_have_value(plot_field)


