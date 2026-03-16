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
    create_gas_work_page.block_select_organization.toggle_should_be_disabled()
    create_gas_work_page.block_select_organization.check_visible_performing_team_label()
    create_gas_work_page.block_select_organization.click_select_team()
    create_gas_work_page.check_required_fields()
    create_gas_work_page.work_data.fill_name_field('Газ')
    create_gas_work_page.work_data.chek_visible_name_field('Газ')
    create_gas_work_page.work_data.click_temperature_measurement_toggle()
    create_gas_work_page.work_data.temperature_measurement_toggle_should_be_enabled()
    create_gas_work_page.work_data.click_nightly_work_toggle()
    create_gas_work_page.work_data.nightly_work_toggle_should_be_enabled()
    create_gas_work_page.work_data.click_holiday_work_toggle()
    create_gas_work_page.work_data.holiday_work_toggle_should_be_enabled()
    create_gas_work_page.work_data.click_is_planned_repair_work_toggle()
    create_gas_work_page.work_data.is_planned_repair_work_toggle_should_be_enabled()
    create_gas_work_page.dates_and_time_component.fill_start_date()
    time.sleep(2)
    create_gas_work_page.dates_and_time_component.fill_stop_date()
    create_gas_work_page.dates_and_time_component.fill_start_time()
    create_gas_work_page.dates_and_time_component.fill_stop_time()
    create_gas_work_page.footer_buttons_component.click_low_save()

    time.sleep(3)







