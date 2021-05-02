import pytest

from pytest_bdd import scenarios, given, when, then

from conf import Constants
from utils.selenium_utils import check_info_and_display

from page_components.login import LoginPage
from page_components.profile import ProfilePage

# Scenarios

scenarios('profile/edit_profile.feature', features_base_dir=Constants.FEATURE_FILES_BASE_DIR)

# Fixtures
@pytest.fixture
def login_page(getBrowser):
    alogin = LoginPage(getBrowser)
    return alogin

@pytest.fixture
def profile_page(getBrowser):
    aProfile = ProfilePage(getBrowser)
    return aProfile

# private method
    
# Given Steps

@given('login with <username> and <currentpwd>')
def login(getBrowser, login_page, username, currentpwd):
    getBrowser.get(Constants.get_buggycar_host())
    login_page.login_with_usename(username, currentpwd)

@given('goto profile page')
def goto_profile(login_page):
    login_page.goto_profile()

# When Steps

@when('look the profile info')
def look():
    # stub function
    pass

@when('the user update with <firstname>, <lastname>, <gender>, <age>, <address>, <phone>, <hobby>')
def update_profile(profile_page, firstname, lastname, gender, age, address, phone, hobby):
    profile_page.set_first_name(firstname)
    profile_page.set_last_name(lastname)
    profile_page.set_gender(gender)
    profile_page.set_age(age)
    profile_page.set_address(address)
    profile_page.set_phone(phone)
    profile_page.set_hobby(hobby)
    # according to requirement, keep it empty unless changing password
    profile_page.current_pwd_onChange_empty()
    profile_page.save()

@when('the user erase <input>')
def erase_input(profile_page, input):
    if input == 'firstname':
        profile_page.firstname_onChange_empty()
    elif input == 'lastname':
        profile_page.lastname_onChange_empty()

@when('the user input <newpassword>')
def input_newpwd(profile_page, newpassword):
    profile_page.set_new_pwd(newpassword)

@when('the user input wrong <confirmpassword>')
def input_confirm_pwd(profile_page, confirmpassword):
    profile_page.set_confirm_pwd(confirmpassword)

@when('the user update <currentpwd> with <newpassword> and <confirmpassword>')
def update_pwd(profile_page, currentpwd, newpassword, confirmpassword):
    profile_page.set_current(currentpwd)
    profile_page.set_new_pwd(newpassword)
    profile_page.set_confirm_pwd(confirmpassword)
    profile_page.save()

# Then Steps

@then('profile updates successfully <successMsg>')
def profile_success_info(profile_page, successMsg):
    result = profile_page.get_success_info()
    assert successMsg == result.text
    assert True == result.is_displayed

@then('login successfully with <username> and <newpassword>')
def login_with_new(login_page, username, newpassword):
    login_page.logout()
    login_page.login_with_usename(username, newpassword)
    assert login_page.check_login() == True

@then('<input> display <errormsg>')
def display_error(profile_page, input, errormsg):
    if input == 'firstname':
        state = profile_page.get_firstname_error()
        check_info_and_display(state, errormsg, True)
    elif input == 'lastname':
        state = profile_page.get_lastname_error()
        check_info_and_display(state, errormsg, True)

@then('save btn is disabled')
def check_register_btn_disabled(profile_page):
    btn_status = profile_page.check_sav_btn_status()
    assert btn_status == False

@then("display <errormsg> show password doesn't match")
def display_pwd_mismatch_error(profile_page, errormsg):
    state = profile_page.get_pwd_mismatch_error()
    check_info_and_display(state, errormsg, True)

@then("correctly display <username>, <firstname>, <lastname>, <gender>, <age>, <address>, <phone>, <hobby>")
def check_profile_info(profile_page, username, firstname, lastname, gender, age, address, phone, hobby):
    actual_username = profile_page.get_username()
    actual_firstname = profile_page.get_firstname()
    actual_lastname = profile_page.get_lastname()
    actual_gender = profile_page.get_gender()
    actual_age = profile_page.get_age()
    actual_address = profile_page.get_address()
    actual_phone = profile_page.get_phone()
    actual_hobby = profile_page.get_hobby()
    assert username == actual_username
    assert firstname == actual_firstname
    assert lastname == actual_lastname
    assert gender == actual_gender
    assert age == actual_age
    assert address == actual_address
    assert phone == actual_phone
    assert hobby == actual_hobby



