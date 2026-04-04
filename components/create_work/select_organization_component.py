from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from pages.base_page import BasePage


class BlockSelectOrganizationComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.base_page = BasePage(page)

        self.toggle = page.locator("label:has-text('Использовать сотрудников ПО')")
        self.team_field = page.locator("//input[@id='performing_team_id']")
        self.contracting_organization_field = page.locator("//input[@id='performing_contractor_id']")
        self.performing_team_label = page.locator("//label[@id='performing_team_id-control-label']")
        self.performing_contracting_organization_label = page.locator(
            "//label[@id='performing_contractor_id-control-label']")
        self.condition_toggle = page.locator(
            "//input[@id='performed_by_contractor']/following-sibling::span[contains(@class,'toggle-presentation')]")
        self.select_first_team = page.locator("(//div/div[contains(@class,'node_name')])[1]")

    def click_select_first_team(self):
        self.select_first_team.click()

    def click_toggle(self):
        self.toggle.is_enabled()
        self.toggle.click()

    def toggle_should_to_be_checked(self):
        expect(self.toggle).to_be_checked()

    def toggle_should_not_to_be_checked(self):
        expect(self.toggle).not_to_be_checked()

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



