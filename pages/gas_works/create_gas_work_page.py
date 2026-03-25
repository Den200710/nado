
from playwright.sync_api import Page

from components.modal_windows.modal_recommended_certification_component import ModalRecommendedCertificationComponent
from components.right_window.right_window_component import RightWindowComponent
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

        self.block_select_organization_component = BlockSelectOrganizationComponent(page)
        self.work_data_component = WorkDataComponent(page)
        self.dates_and_time_component = DatesComponent(page)
        self.approvers_person_component = ApproversComponent(page)
        self.footer_buttons_component = FooterButtonsComponent(page)
        self.right_window_component = RightWindowComponent(page)
        self.modal_recommended_certification = ModalRecommendedCertificationComponent(page)

        self.permit_issuer = ResponsiblePersonsComponent(page, 'permit_issuer')
        self.executor = ResponsiblePersonsComponent(page, 'executor')
        self.admitter = ResponsiblePersonsComponent(page, 'admitter')
        self.representative_gss = ResponsiblePersonsComponent(page, 'representative_gss')
        self.shift_supervisor = ResponsiblePersonsComponent(page, 'shift_supervisor')

    def check_required_fields(self):
        self.check_after(self.permit_issuer.responsible_person_label, should_have_after=True)
        self.check_after(self.executor.responsible_person_label, should_have_after=True)
        self.check_after(self.admitter.responsible_person_label, should_have_after=True)
        self.check_after(self.representative_gss.responsible_person_label, should_have_after=True)
        self.check_after(self.shift_supervisor.responsible_person_label, should_have_after=True)
        self.check_after(self.work_data_component.name_label, should_have_after=True)

    def click_select_permit_issuer(self):
        self.permit_issuer.click_responsible_person_field()

    def click_select_executor(self):
        self.executor.click_responsible_person_field()

    def click_select_admitter(self):
        self.admitter.click_responsible_person_field()

    def click_select_representative_gss(self):
        self.representative_gss.click_responsible_person_field()

    def click_select_shift_supervisor(self):
        self.shift_supervisor.click_responsible_person_field()

    def click_first_responsible_in_list(self):
        self.permit_issuer.click_select_first_responsible_in_list()

