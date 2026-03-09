
import pytest

from pages.authentication.login_page import LoginPage
from pages.monitoring.operational_plan_page import OperationalPlanPage


creds = {
    ('test17@test.test', '123654'): 'User company',
    ('liya.gaysina.02@mail.ru', '123654'): 'User contracting organization'
}


@pytest.mark.parametrize('email, password', creds.keys(), ids=creds.values())
def test_successful_authorization(login_page: LoginPage,
                                  operational_plan_page: OperationalPlanPage,
                                  email: str,
                                  password: str):
    login_page.visit('http://nuzhno2.lan/')
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    operational_plan_page.check_visible_main_title()

