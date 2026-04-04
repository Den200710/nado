from playwright.sync_api import Page
from datetime import datetime, timedelta

from components.base_component import BaseComponent



class DatesComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.date_start_label = page.locator("//label[@id='start_date-control-label']")
        self.date_start_input = page.locator("//input[@id='start_date']")
        self.date_end_label = page.locator("//label[@id='stop_date-control-label']")
        self.date_end_input = page.locator("//input[@id='stop_date']")
        self.time_start_label = page.locator("//label[@id='start_time-control-label']")
        self.time_start_input = page.locator("//input[@id='start_time']")
        self.time_end_label = page.locator("//label[@id='stop_time-control-label']")
        self.time_end_input = page.locator("//input[@id='stop_time']")



    def fill_start_date(self, date = datetime.now().strftime('%d-%m-%Y')):
        self.date_start_input.click()
        self.date_start_input.fill(date)
        self.date_start_input.is_visible()
        assert self.date_start_input.input_value() != "", "Поле пустое"
        self.page.keyboard.press('Tab')


    def fill_stop_date(self, date = datetime.now().strftime('%d-%m-%Y')):
        self.date_end_input.fill(date)
        assert self.date_end_input.input_value() != "", "Поле пустое"
        self.page.keyboard.press('Tab')

    def fill_start_time(self, time = datetime.now().strftime('%H:%M')):
        self.time_start_input.fill(time)
        assert self.time_start_input.input_value() != "", "Поле пустое"
        self.page.keyboard.press('Tab')

    def fill_stop_time(self):
        time = datetime.now() + timedelta(minutes=1)
        time_str = time.strftime('%H:%M')
        self.time_end_input.fill(time_str)
        assert self.time_end_input.input_value() != "", "Поле пустое"



