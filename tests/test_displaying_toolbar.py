import time

from pages.monitoring.operational_plan_page import OperationalPlanPage
from pages.gas_works.to_approval_works_page import ToApprovalWorksPage
from pages.gas_works.current_works_page import CurrentWorksPage
from pages.gas_works.all_works_page import AllWorksPage
from pages.gas_works.create_gas_work_page import CreateGasWorkPage
from components.toolbar.toolbar_component import ToolbarComponent


def test_displaying_toolbar_on_gas_work_pages(
        operational_plan_page: OperationalPlanPage,
        to_approval_page: ToApprovalWorksPage,
        current_works_page: CurrentWorksPage,
        all_works_page: AllWorksPage,
        create_gas_work_page: CreateGasWorkPage,
        toolbar_component: ToolbarComponent
):
    operational_plan_page.check_visible_main_title()
    operational_plan_page.sidebar.click_gas_works_item()
    to_approval_page.check_title_page.check_visible_page_title("Газоопасные работы на согласовании")
    toolbar_component.click_create_work_button()
    create_gas_work_page.block_select_organization.click_toggle()
    create_gas_work_page.block_select_organization.check_condition_toggle('Да')
    create_gas_work_page.block_select_organization.check_visible_performing_contracting_organization_label()
    create_gas_work_page.block_select_organization.click_select_contracting_organization()
    create_gas_work_page.permit_issuer.check_required_field(True)
    create_gas_work_page.executor.check_required_field(True)
    create_gas_work_page.admitter.check_required_field(True)
    create_gas_work_page.shift_supervisor.check_required_field(False)
    create_gas_work_page.representative_gss.check_required_field(True)
    create_gas_work_page.permit_issuer.click_select_responsible()

    time.sleep(1)







