
from playwright.sync_api import Page
from pages.base_page import BasePage
from components.work.select_organization_component import BlockSelectOrganizationComponent
from components.work.responsible_persons_component import ResponsiblePersonsComponent


class CreateGasWorkPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.block_select_organization = BlockSelectOrganizationComponent(page)

        self.permit_issuer = ResponsiblePersonsComponent(page, 'permit_issuer')
        self.executor = ResponsiblePersonsComponent(page, 'executor')
        self.admitter = ResponsiblePersonsComponent(page, 'admitter')
        self.representative_gss = ResponsiblePersonsComponent(page, 'representative_gss')
        self.shift_supervisor = ResponsiblePersonsComponent(page, 'shift_supervisor')


