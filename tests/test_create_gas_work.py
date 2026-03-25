import time

from pages.monitoring.operational_plan_page import OperationalPlanPage
from pages.gas_works.to_approval_works_page import ToApprovalWorksPage
from pages.gas_works.create_gas_work_page import CreateGasWorkPage
from components.toolbar.toolbar_component import ToolbarComponent


def test_displaying_toolbar_on_gas_work_pages(
        operational_plan_page: OperationalPlanPage,
        to_approval_page: ToApprovalWorksPage,
        create_gas_work_page: CreateGasWorkPage,
        toolbar_component: ToolbarComponent
):
    operational_plan_page.check_visible_main_title() # Проверка заголовка
    operational_plan_page.sidebar.click_gas_works_item() # Клик га Газоопасные работы
    to_approval_page.check_title_page.check_visible_page_title("Газоопасные работы на согласовании") # Проверка открытия
    toolbar_component.click_create_work_button() # Клик создать работу
    create_gas_work_page.block_select_organization_component.toggle_should_not_to_be_checked() # Выключен флаг ПО
    create_gas_work_page.block_select_organization_component.check_visible_performing_team_label() # Проверка заголовка СП
    create_gas_work_page.block_select_organization_component.click_select_team() # Выбор СП
    create_gas_work_page.block_select_organization_component.click_select_first_team() # Выбор первого СП 1
    create_gas_work_page.check_required_fields() # Проверка всех основных полей на обязательность
    create_gas_work_page.click_select_permit_issuer()
    create_gas_work_page.click_first_responsible_in_list()
    create_gas_work_page.click_select_executor()
    create_gas_work_page.click_first_responsible_in_list()
    create_gas_work_page.click_select_representative_gss()
    create_gas_work_page.click_first_responsible_in_list()
    create_gas_work_page.click_select_shift_supervisor()
    create_gas_work_page.click_first_responsible_in_list()
    create_gas_work_page.click_select_admitter()
    create_gas_work_page.click_first_responsible_in_list()
    create_gas_work_page.work_data_component.fill_name_field('Газ') # Заполняем название
    create_gas_work_page.work_data_component.chek_visible_name_field('Газ') # Проверка отображения названия
    create_gas_work_page.work_data_component.click_select_team()
    create_gas_work_page.block_select_organization_component.click_select_first_team()  # Выбор СП 2
    create_gas_work_page.work_data_component.click_work_kind_field() # Вид работы
    create_gas_work_page.work_data_component.click_select_first_kind_work() # Первый вид
    create_gas_work_page.work_data_component.click_specificity_field()
    create_gas_work_page.work_data_component.click_select_specificity_output()
    create_gas_work_page.work_data_component.click_place_work_button()
    create_gas_work_page.work_data_component.click_select_first_work_place()
    create_gas_work_page.right_window_component.click_close_right_window()

    # create_gas_work_page.work_data_component.click_temperature_measurement_toggle() # Клик переключатель температуры
    # create_gas_work_page.work_data_component.temperature_measurement_toggle_should_be_enabled() # Проверка, что включен
    create_gas_work_page.work_data_component.click_nightly_work_toggle() # Проверка, что включен
    create_gas_work_page.work_data_component.nightly_work_toggle_should_be_enabled() # Проверка, что включен
    # create_gas_work_page.work_data_component.click_holiday_work_toggle() # Клик праздничные дни
    # create_gas_work_page.work_data_component.holiday_work_toggle_should_be_enabled() # Проверка, что включен
    # create_gas_work_page.work_data_component.click_is_planned_repair_work_toggle() # Клик ремонтные работы
    # create_gas_work_page.work_data_component.is_planned_repair_work_toggle_should_be_enabled() # Проверка, что включен

    create_gas_work_page.approvers_person_component.click_labor_protection_field()
    create_gas_work_page.click_first_responsible_in_list()
    create_gas_work_page.approvers_person_component.click_department_pkpb_field()
    create_gas_work_page.click_first_responsible_in_list()
    create_gas_work_page.approvers_person_component.click_representative_gss_field()
    create_gas_work_page.click_first_responsible_in_list()
    create_gas_work_page.approvers_person_component.click_approver_field()
    create_gas_work_page.click_first_responsible_in_list()

    create_gas_work_page.dates_and_time_component.fill_start_date()
    create_gas_work_page.dates_and_time_component.fill_stop_date()
    create_gas_work_page.dates_and_time_component.fill_start_time()
    create_gas_work_page.dates_and_time_component.fill_stop_time()
    create_gas_work_page.footer_buttons_component.click_low_save()

    create_gas_work_page.modal_recommended_certification.check_modal_certification_title()
    create_gas_work_page.modal_recommended_certification.click_reject_recommended_certification()

    time.sleep(3)







