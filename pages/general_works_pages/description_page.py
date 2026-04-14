from __future__ import annotations

from playwright.sync_api import Page

from components.create_work.approvers_component import ApproversComponent
from components.create_work.select_organization_component import BlockSelectOrganizationComponent
from components.create_work.work_data_component import WorkDataComponent
from components.created_work.dangerous_data_component import DangerousDataComponent
from components.created_work.responsible_agreed_component import ResponsibleAgreedComponent
from components.created_work.responsible_employee_component import ResponsibleEmployeeComponent
from pages.base_page import BasePage
from components.navigation.work_page_tabs_component import WorkPageTabsComponent

class DescriptionPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.work_tabs = WorkPageTabsComponent(page)
        self.work_data_component = WorkDataComponent(page)
        self.dangerous_data = DangerousDataComponent(page)
        self.select_organization_component = BlockSelectOrganizationComponent(page)
        self.responsible_data_component = ResponsibleEmployeeComponent(page)
        self.responsible_employee = ResponsibleEmployeeComponent(page)
        self.approvers_component = ApproversComponent(page)
        self.responsible_agreed_component = ResponsibleAgreedComponent(page)

    def verify_responsible_persons_match_created(self, created_data: dict) -> None:
        """Проверка ответственных лиц"""
        responsible_fields = [
            ('permit_issuer', 'permit_issuer', 'Permit issuer'),
            ('executor', 'executor', 'Executor'),
            ('admitter', 'admitter', 'Admitter'),
            ('representative_gss', 'representative_gss', 'Representative GSS'),
            ('shift_supervisor', 'shift_supervisor', 'Shift supervisor'),
        ]

        for actual_key, expected_key, field_name in responsible_fields:
            self.verify_field(
                self.responsible_employee.get_value(actual_key),
                created_data.get(expected_key, ''),
                field_name,
                normalize=False
            )

    def verify_approvers_match_created(self, created_data: dict) -> None:
        """Проверка апруверов (согласующих лиц)"""
        approver_person_fields = [
            ('supervisor_team', 'supervisor_team', 'Supervisor team'),
            ('labor_protection', 'labor_protection', 'Labor protection'),
            ('department_pkpb', 'department_pkpb', 'Department PKPB'),
            ('representative_gss', 'representative_gss', 'Representative GSS'),
            ('approver', 'approver', 'Approver'),
        ]

        for actual_key, expected_key, field_name in approver_person_fields:
            actual_value = self.responsible_agreed_component.get_value_person(actual_key)
            expected_value = created_data.get(expected_key, '')
            self.verify_field(
                actual_value,
                expected_value,
                f"Approver person - {field_name}",
                normalize=False
            )

        approver_position_fields = [
            ('supervisor_team_position', 'supervisor_team_position', 'Supervisor team position'),
            ('labor_protection_position', 'labor_protection_position', 'Labor protection position'),
            ('department_pkpb_position', 'department_pkpb_position', 'Department PKPB position'),
            ('representative_gss_position', 'representative_gss_position', 'Representative GSS position'),
            ('approver_position', 'approver_position', 'Approver position'),
        ]

        for actual_key, expected_key, field_name in approver_position_fields:
            actual_value = self.responsible_agreed_component.get_value_position(actual_key)
            expected_value = created_data.get(expected_key, '')
            self.verify_field(
                actual_value,
                expected_value,
                f"Approver position - {field_name}",
                normalize=True
            )

    def verify_dangerous_data_matches_created(self, created_data: dict) -> None:
        self._data_fields = [
            ('name', 'name', 'Name', False),
            ('plot', 'plot', 'Plot', True),
            ('work_kind', 'work_kind', 'Work kind', False),
            ('work_plan', 'work_plan', 'Work_plan', True),
            ('nightly_work', 'nightly_work', 'Nightly_work', False),
            ('temperature_measurement', 'temperature_measurement', 'Temperature_measurement', False),
            ('order', 'order', 'Order', True),
            ('specificity', 'specificity', 'Work_specificity', False),
            ('performing_team', 'performing_team', 'Performing_team', False),
            ('holiday_work', 'holiday_work', 'Holiday_work', False),
            ('character_work', 'description', 'Character_work', True)
        ]

        for actual_key, expected_key, field_name, need_normalize in self._data_fields:
            self.verify_field(
                self.dangerous_data.get_value(actual_key),
                created_data.get(expected_key, ''),
                field_name,
                need_normalize
            )
        self.verify_responsible_persons_match_created(created_data)
        self.verify_approvers_match_created(created_data)



