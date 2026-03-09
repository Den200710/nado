

from pages.monitoring.operational_plan_page import OperationalPlanPage
from pages.gas_works.to_approval_works_page import ToApprovalWorksPage


def test_operational_plan_displaying(
        operational_plan_page: OperationalPlanPage,
        to_approval_page: ToApprovalWorksPage
):
    operational_plan_page.check_visible_main_title()
    operational_plan_page.sidebar.click_gas_works_item()
    to_approval_page.check_title_page.check_visible_page_title("Газоопасные работы на согласовании")
