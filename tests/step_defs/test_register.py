import pytest

from pytest_bdd import scenarios, given, when, then
from conf import Constants
from page_components.register import RegisterPage
from page_components.login import LoginPage


# Scenarios

scenarios('auth/register.feature', features_base_dir=Constants.FEATURE_FILES_BASE_DIR)

# Fixtures
@pytest.fixture
def login_page(getBrowser):
    alogin = LoginPage(getBrowser)
    return alogin

@pytest.fixture
def register_page(getBrowser):
    aRegister = RegisterPage(getBrowser)
    return aRegister

# private method
    
# Given Steps

@given('Go to register page')
def get_register(getBrowser):
    getBrowser.get(Constants.get_register_url())

# When Steps

@when('the user register with <username> <firstname> <lastname> <password> and <confirmpassword>')
def register(register_page, username, firstname, lastname, password, confirmpassword):
    register_page.register_all(username, firstname, lastname, password, confirmpassword)

@when('the user input <firstname> <lastname> <password> and <confirmpassword>')
def register_without_username(register_page, firstname, lastname, password, confirmpassword):
    register_page.input_firstname(firstname)
    register_page.input_lastname(lastname)
    register_page.input_password(password)
    register_page.input_confirmpassword(confirmpassword)

@when('the user input wrong <confirmpassword>')
def input_wrong_conform(register_page, confirmpassword):
    register_page.input_confirmpassword(confirmpassword)

@when('the user input correct <username> <firstname> <lastname> <password> <confirmpassword>')
def input_info(register_page, username, firstname, lastname, password, confirmpassword):
    register_page.input_username(username)
    register_page.input_firstname(firstname)
    register_page.input_lastname(lastname)
    register_page.input_password(password)
    register_page.input_confirmpassword(confirmpassword)

@when('the user input correct <username> <firstname> <lastname> <password>')
def input_info(register_page, username, firstname, lastname, password):
    register_page.input_username(username)
    register_page.input_firstname(firstname)
    register_page.input_lastname(lastname)
    register_page.input_password(password)

@when('the user erase <input>')
def erase_info(register_page, input):
    if input == 'username':
        register_page.clear_username_input()
    elif input == 'firstname':
        register_page.clear_firstname_input()
    elif input == 'lastname':
        register_page.clear_lastname_input()
    elif input == 'password':
        register_page.clear_password_input()
    elif input == 'confirm':
        register_page.clear_confirm_input()
    else:
        raise Exception('not support input name')

# Then Steps

@then('register successfully and show <successfulMsg>')
def reg_success_info(register_page, successfulMsg):
    result = register_page.get_success_info()
    assert successfulMsg == result
    assert register_page.check_success_info_display() == True
    
@then('register btn is disabled')
def check_register_btn_disabled(register_page):
    btn_status = register_page.check_reg_btn_enabled()
    assert btn_status == False

@then('can login with <username> and <password>')
def can_login(login_page, username, password):
    login_page.login_with_usename(username, password)
    profile = login_page.get_profile_link()
    # assert already login 
    assert profile.text != ''

@then('register unsuccessfully and error message <error> is displayed')
def check_register_unsuccess(register_page, error):
    error_info = register_page.get_error_info()
    assert error_info == error

@then("display <errormsg> show password doesn't match")
def show_confirm_not_match(register_page, errormsg):
    state = register_page.get_confirm_error()
    __check_info_and_display(state, errormsg, True)

@then('<input> display <errormsg>')
def show_errorMsg_input(register_page, input, errormsg):
    if input == 'username':
        state = register_page.get_username_error()
        __check_info_and_display(state, errormsg, True)
    elif input == 'firstname':
        state = register_page.get_firstname_error()
        __check_info_and_display(state, errormsg, True)
    elif input == 'lastname':
        state = register_page.get_lastname_error()
        __check_info_and_display(state, errormsg, True)
    elif input == 'password':
        state = register_page.get_password_error()
        __check_info_and_display(state, errormsg, True)
    elif input == 'confirm':
        state = register_page.get_confirm_error()
        __check_info_and_display(state, errormsg, True)
    else:
        raise Exception('not support input name')
    
def __check_info_and_display(state, errormsg, is_displayed):
    assert state.text == errormsg
    assert state.is_displayed == is_displayed