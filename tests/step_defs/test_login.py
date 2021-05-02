import pytest

from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.keys import Keys
from conf import Constants
from selenium.webdriver.support.ui import WebDriverWait
from page_components.login import LoginPage


# Scenarios

scenarios('auth/login.feature', features_base_dir=Constants.FEATURE_FILES_BASE_DIR)

# Fixtures
@pytest.fixture
def login_page(getBrowser):
    alogin = LoginPage(getBrowser)
    return alogin

def _login_with_username_passwd(page, username, password):
    page.login_with_usename(username, password)

# Given Steps

@given('Go to Home page')
def get_login(getBrowser):
    getBrowser.get(Constants.get_buggycar_host())

@given('the user has been registered correctly')
def register_user():
    # in this fucntion, ideally can directly insert data into database 
    # for this login test
    # remove any dependency with the action on register page
    # at this moment, we just use the pre-added data, igonre this function
    pass

@given('the user has login with <username> and <password>')
def prepare_login_state(login_page, username, password):
    _login_with_username_passwd(login_page, username, password)

# When Steps

@when('the user inputs <username> and <password>')
def login_with_correct_credential(login_page, username, password):
    _login_with_username_passwd(login_page, username, password)


@when('the user inputs wrong <username> and <password>')
def login_with_wrong_credential(login_page, username, password):
    _login_with_username_passwd(login_page, username, password)

@when('the user logout')
def logout(login_page):
    login_page.logout()

# Then Steps

@then('login successfully and <name> should be displayed')
def success_show_name(getBrowser, login_page, name):
    result = login_page.get_login_name()
    assert 'Hi, ' + name == result
    
    
@then('error message is displayed')
def fail_login_message(getBrowser, login_page):
    result = login_page.get_login_failed_msg()
    assert 'Invalid username/password' == result

@then('the user successfully logout')
def check_module(getBrowser, login_page):
    is_logout = login_page.check_logout()
    is_can_login_again = login_page.check_login_elements()
    # assert already logout and login elements can displayed again
    assert is_logout == True
    assert is_can_login_again == True