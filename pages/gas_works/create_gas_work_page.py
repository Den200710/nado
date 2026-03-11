from playwright.sync_api import Page
from pages.base_page import BasePage

from components.work.select_organization_component import BlockSelectOrganizationComponent


class CreateGasWorkPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.block_select_organization = BlockSelectOrganizationComponent(page)


