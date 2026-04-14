from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from pages.base_page import BasePage


class WorkDataComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_page = BasePage(page)

        # Словарь с полями ввода
        self._input_fields = {
            'name': page.locator("//input[@id='name']"),
            'performing_team': page.locator("//input[@id='team_id']"),
            'work_kind': page.locator("//input[@id='lib_work_kind_id']"),
            'work_plan': page.locator("//input[@id='work_plan_id']"),
            'description': page.locator("//textarea[@id='work_description']"),
            'order': page.locator("//textarea[@id='order_name']"),
            'plot': page.locator("(//div[contains(@class,'form-control')]//textarea)[3]"),
            'specificity': page.locator("//span[contains(text(),'Работы производятся')]")
        }
        # Словарь с переключателями
        self._toggles = {
                'nightly_work': page.locator("//label[contains(@class,'toggle')][input[@id='nightly']]"),
                'temperature_measurement': page.locator(
                    "//label[contains(@class,'toggle')][input[@id='measurement_required']]"),
                'holiday_work': page.locator(
                    "//label[contains(@class,'toggle')][input[@id='weekend']]"),
                'planned_repair': page.locator(
                    "//label[contains(@class,'toggle')][input[@id='is_planned_maintenance_work']]")
        }

        self.name_label = page.locator("//label[@id='name-control-label']")
        self.team_label = page.locator("//label[@id='team_id-control-label']")
        self.work_kind_label = page.locator("//label[@id='lib_work_kind_id-control-label']")
        self.work_plan_label = page.locator("//label[@id='work_plan_id-control-label']")
        self.description_label = page.locator("//label[@id='work_description-control-label']")
        self.specificity_label = page.locator("//label[@id='lib_specificity_id-control-label']")
        self.specificity_field = page.locator("//div[contains(@class,'picker-select')]/div[contains(@class,'picker')]")
        self.select_specificity_out = page.locator("//span[text()='Работы производятся на открытой площадке']")
        self.select_specificity_into = page.locator(
            "//span[text()='Работы производятся в замкнутом пространстве (колодец, сосуд, цистерна)']")
        self.order_name_label = page.locator("//label[@id='order_name-control-label']")
        self.temperature_measurement_label = page.locator("//label[@id='measurement_required-control-label']")
        self.nightly_work_label = page.locator("//label[@id='nightly-control-label']")
        self.holiday_work_label = page.locator("//label[@id='weekend-control-label']")
        self.is_planned_repair_work_label = page.locator("//label[@id='is_planned_maintenance_work-control-label']")
        self.place_work_label = page.locator("//label[text()='Место проведения работы']")
        self.place_work_field = page.locator(
            "(//div[contains(@class,'form-control')]//div[contains(@class,'empty-data')])[1]")
        self.place_work_button = page.locator("//div[contains(@class,'view-block_header')]//span[text()='Выбрать']")
        self.plot_label = page.locator("//div[text()='Участок']")
        self.select_first_work_place = page.locator("(//div[contains(text(),'Трубопроводы')])[1]")
        self.select_first_kind_work = page.locator("(//div[contains(text(), 'Установка заглушек')])[1]")
        # self.approver_certification_label = page.locator("//label[@id='approverCertifications-control-label']")
        # self.approver_certification_field = page.locator("(//div[contains(@class,'multiple-select')])[3]")
        # self.approver_certification_select_button = page.locator(
        #     "(//div[contains(@class,'multiple-select_actions')]/button)[1]")
        # self.approver_certification_clear_button = page.locator(
        #     "(//div[contains(@class,'multiple-select_actions')]/button)[2]")
        # self.approver_contracting_certification_label = page.locator(
        #     "//label[@id='approverCertificationsForContractingEmployee-control-label']")
        # self.approver_contracting_certification_field = page.locator()

    def fill_field(self, field_name: str, value: str) -> None:
        """Заполнить поле по имени"""
        locator = self._input_fields.get(field_name)
        if not locator:
            raise KeyError(f"Field '{field_name}' not found")
        locator.fill(value)

    def check_visible_name_field(self, name: str):
        expect(self._input_fields['name']).to_have_value(name)

    def click_select_team(self):
        self._input_fields['performing_team'].click()

    def click_work_kind_field(self):
        self._input_fields['work_kind'].click()

    def click_work_plan_field(self):
        self._input_fields['work_plan'].click()

    def check_visible_description_field(self, description: str):
        expect(self._input_fields['description']).to_have_value(description)

    def click_specificity_field(self):
        self.specificity_field.click()

    def click_select_specificity_output(self):
        self.select_specificity_out.click()

    def click_select_specificity_into(self):
        self.select_specificity_into.click()

    def check_visible_order_name_field(self, order_name: str):
        expect(self._input_fields['order_name']).to_have_value(order_name)

    def check_visible_place_work_field(self):
        expect(self.place_work_field).to_be_visible()

    def click_toggle(self, toggle_name: str) -> None:
        """Кликнуть по переключателю"""
        locator = self._toggles.get(toggle_name)
        locator.click()

    def temperature_measurement_toggle_should_be_enabled(self):
        expect(self._toggles['temperature_measurement']).to_be_checked()

    def temperature_measurement_toggle_should_be_disabled(self):
        expect(self._toggles['temperature_measurement']).not_to_be_checked()

    def nightly_work_toggle_should_be_enabled(self):
        expect(self._toggles['nightly_work']).to_be_checked()

    def nightly_work_toggle_should_be_disabled(self):
        expect(self._toggles['nightly_work']).not_to_be_checked()

    def holiday_work_toggle_should_be_enabled(self):
        expect(self._toggles['holiday_work']).to_be_checked()

    def holiday_work_toggle_should_be_disabled(self):
        expect(self._toggles['holiday_work']).not_to_be_checked()

    def is_planned_repair_work_toggle_should_be_enabled(self):
        expect(self._toggles['planned_repair']).to_be_checked()

    def is_planned_repair_work_toggle_should_be_disabled(self):
        expect(self._toggles['planned_repair']).not_to_be_checked()

    def click_place_work_button(self):
        self.place_work_button.click()

    def check_visible_plot_field_field(self, plot_field: str):
        expect(self._input_fields['plot']).to_have_value(plot_field)

    def click_select_first_work_place(self):
        self.select_first_work_place.click()

    def click_select_first_kind_work(self):
        self.select_first_kind_work.click()

    def get_field_value(self, field_name: str) -> str:
        """Получить значение поля по имени (работает с любыми элементами)"""
        locator = self._input_fields.get(field_name)
        if not locator:
            raise KeyError(f"Field '{field_name}' not found")
        value = None
        try:
            value = locator.input_value()
        except Exception:
            pass
        if value is None:
            value = locator.get_attribute("value")
        if not value:
            value = locator.text_content()
        return value.strip() if value else ''

    def get_toggle_state(self, toggle_name: str) -> bool:
        """Получить состояние переключателя"""
        locator = self._toggles.get(toggle_name)
        if not locator:
            raise KeyError(f"Toggle '{toggle_name}' not found")
        return locator.is_checked()

    def get_all_work_data(self) -> dict:
        """Получить все данные"""
        return {
            'name': self.get_field_value('name'),
            'plot': self.get_field_value('plot'),
            'description': self.get_field_value('description'),
            'work_kind': self.get_field_value('work_kind'),
            'work_plan': self.get_field_value('work_plan'),
            'nightly_work': self.get_toggle_state('nightly_work'),
            'temperature_measurement': self.get_toggle_state('temperature_measurement'),
            'order': self.get_field_value('plot'),
            'specificity': self.get_field_value('specificity'),
            'performing_team': self.get_field_value('performing_team'),
            'holiday_work': self.get_toggle_state('holiday_work'),
        }



