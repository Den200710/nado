from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class ModalRecommendedCertificationComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.modal_certification_title = page.locator("//div[contains(@class,'modal-header')]")
        self.confirm_recommended_certification = page.locator("//button[text()='Да']")
        self.reject_recommended_certification = page.locator("//button[text()='Нет']")

    def check_modal_certification_title(self):
        expect(self.modal_certification_title).to_be_visible()
        expect(self.modal_certification_title).to_have_text('Дополнить список аттестаций рекомендуемыми аттестациями?')

    def click_confirm_recommended_certification(self):
        self.confirm_recommended_certification.click()

    def click_reject_recommended_certification(self):
        self.reject_recommended_certification.click()