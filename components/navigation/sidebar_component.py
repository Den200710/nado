import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.gas_works_list_item = SidebarListItemComponent(page, 'Газоопасные работы')
        self.flammable_works_list_item = SidebarListItemComponent(page, 'Огневые работы')
        self.altitude_works_list_item = SidebarListItemComponent(page, 'Работы на высоте')
        self.earth_works_list_item = SidebarListItemComponent(page, 'Земляные работы')
        self.repair_works_list_item = SidebarListItemComponent(page, 'Ремонтные работы')

    def click_gas_works_item(self):
        self.gas_works_list_item.navigate_url(re.compile(r".*/nado/gas-work/to-approval"))

    def click_flammable_works_item(self):
        self.flammable_works_list_item.navigate_url(re.compile(r".*/nado/flammable-work/to-approval"))

    def click_altitude_works_item(self):
        self.altitude_works_list_item.navigate_url(re.compile(r".*/nado/altitude-work/to-approval"))

    def click_earth_works_item(self):
        self.earth_works_list_item.navigate_url(re.compile(r".*/nado/earth-work/to-approval"))

    def click_repair_works_item(self):
        self.repair_works_list_item.navigate_url(re.compile(r".*/nado/repair-work/to-approval"))
