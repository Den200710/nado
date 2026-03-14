from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from pages.base_page import BasePage


class BlockSelectOrganizationComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.base_page = BasePage(page)

        self.toggle = page.locator("//input[@id='performed_by_contractor']")
        self.team_field = page.locator("//input[@id='performing_team_id']")
        self.contracting_organization_field = page.locator("//input[@id='performing_contractor_id']")
        self.performing_team_label = page.locator("//label[@id='performing_team_id-control-label']")
        self.performing_contracting_organization_label = page.locator(
            "//label[@id='performing_contractor_id-control-label']")
        self.condition_toggle = page.locator(
            "//input[@id='performed_by_contractor']/following-sibling::span[contains(@class,'toggle-presentation')]"
        )

    def click_toggle(self):
        self.toggle.click(force=True)

    def click_select_team(self):
        self.team_field.click()

    def click_select_contracting_organization(self):
        self.contracting_organization_field.click()

    def check_visible_performing_team_label(self):
        expect(self.performing_team_label).to_be_visible()
        self.base_page.check_after(self.performing_team_label, True)

    def check_visible_performing_contracting_organization_label(self):
        expect(self.performing_contracting_organization_label).to_be_visible()
        self.base_page.check_after(self.performing_contracting_organization_label, True)

    def check_condition_toggle(self, condition):
        expect(self.condition_toggle).to_have_text(condition)
