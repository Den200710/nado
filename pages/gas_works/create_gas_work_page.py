
from playwright.sync_api import Page
from pages.base_page import BasePage
from components.work.select_organization_component import BlockSelectOrganizationComponent
from components.work.work_data_component import WorkDataComponent
from components.work.responsible_persons_component import ResponsiblePersonsComponent
from components.work.dates_component import DatesComponent
from components.work.approvers_component import ApproversComponent
from components.work.footer_buttons_component import FooterButtonsComponent


class CreateGasWorkPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.block_select_organization = BlockSelectOrganizationComponent(page)
        self.work_data = WorkDataComponent(page)
        self.dates_and_time_component = DatesComponent(page)
        self.approver_person_component = ApproversComponent(page)
        self.footer_buttons_component = FooterButtonsComponent(page)

        self.permit_issuer = ResponsiblePersonsComponent(page, 'permit_issuer')
        self.executor = ResponsiblePersonsComponent(page, 'executor')
        self.admitter = ResponsiblePersonsComponent(page, 'admitter')
        self.representative_gss = ResponsiblePersonsComponent(page, 'representative_gss')
        self.shift_supervisor = ResponsiblePersonsComponent(page, 'shift_supervisor')

    def check_required_fields(self):
        self.check_after(self.permit_issuer.approver_person_label, should_have_after=True)
        self.check_after(self.executor.approver_person_label, should_have_after=True)
        self.check_after(self.admitter.approver_person_label, should_have_after=True)
        self.check_after(self.representative_gss.approver_person_label, should_have_after=True)
        self.check_after(self.shift_supervisor.approver_person_label, should_have_after=True)
        self.check_after(self.work_data.name_label, should_have_after=True)


