from collections import namedtuple

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utils.selenium_utils import simulate_onChange


class ProfilePage:
    """represent the profile page"""

    USERNAME_INPUT_ID = "username"
    FIRSTNAME_INPUT_ID = "firstName"
    LASTNAME_INPUT_ID = "lastName"
    GENDER_ID = "gender"
    AGE_ID = "age"
    ADDRESS_ID = "address"
    PHONE_ID = "phone"
    HOBBY_ID = "hobby"
    CURRENT_PASSWORD_ID = 'currentPassword'
    NEW_PASSWORD_ID = 'newPassword'
    CONFIRM_PASSWORD_ID = 'newPasswordConfirmation'
    LANG_ID = 'language'

    GENDER_OPTION_XPATH = "//datalist[@id='genders']/option[@value='{}']"

    SAVE_BTN_XPATH = "//button[text()='Save']"
    
    SUCCESS_INFO_CSS = "[class='result alert alert-success hidden-md-down']"
    ERROR_INFO_CSS = "[class='result alert alert-danger hidden-md-down']"

    REQUIRE_FN_MSG_XPATH = "//input[@id='firstName']/following-sibling::div[1]"
    REQUIRE_LN_MSG_XPATH = "//input[@id='lastName']/following-sibling::div[1]"
    REQUIRE_CPW_MSG_XPATH = "//input[@id='newPasswordConfirmation']/following-sibling::div[1]"

    def __init__(self, browser):
        self.browser = browser

    def get_browser(self):
        return self.browser

    def get_success_info(self):
        ElementState = namedtuple('msg',['text', 'is_displayed'])
        element = self.__get_success_info_element()
        state = ElementState(element.text, element.is_displayed())
        return state
    
    def get_error_info(self):
        ElementState = namedtuple('msg',['text', 'is_displayed'])
        element = self.__get_error_info_element()
        state = ElementState(element.text, element.is_displayed())
        return state

    def set_first_name(self, firstname):
        element = self.__get_firstname_input_element()
        element.clear()
        element.send_keys(firstname)
    
    def set_last_name(self, lastname):
        element = self.__get_lastname_input_element()
        element.clear()
        element.send_keys(lastname)
    
    def set_gender(self, gender):
        # for select-based input tag
        gender_ele = self.__get_gender_element()
        gender_ele.send_keys(gender)
        # gender_opt = Select(self.__get_gender_opt(gender))
        # gender_opt.select_by_value(gender)

    def set_age(self, age):
        element = self.__get_age_element()
        element.clear()
        element.send_keys(age)
    
    def set_address(self, address):
        element = self.__get_address_element()
        element.clear()
        element.send_keys(address)
    
    def set_phone(self, phone):
        element = self.__get_phone_element()
        element.clear()
        element.send_keys(phone)
    
    def set_hobby(self, hobby):
        element = Select(self.__get_hobby_element())
        element.select_by_visible_text(hobby)
    
    def set_current(self, current):
        element = self.__get_current_password_element()
        element.clear()
        element.send_keys(current)
    
    def set_new_pwd(self, new_pwd):
        element = self.__get_new_password_element()
        element.clear()
        element.send_keys(new_pwd)
    
    def set_confirm_pwd(self, confirm):
        element = self.__get_confirm_password_elemrnt()
        element.clear()
        element.send_keys(confirm)

    def set_lang(self, lang):
        element = Select(self.__get_lang_element())
        element.select_by_value(lang)
    
    def save(self):
        element = self.__get_save_btn()
        element.click()
    
    def firstname_onChange_empty(self):
        element = self.__get_firstname_input_element()
        simulate_onChange(element)
    
    def lastname_onChange_empty(self):
        element = self.__get_lastname_input_element()
        simulate_onChange(element)

    def current_pwd_onChange_empty(self):
        element = self.__get_current_password_element()
        simulate_onChange(element)
    
    def get_username(self):
        element = self.__get_loginname_input_element()
        return element.get_attribute('value')
    
    def get_firstname(self):
        element = self.__get_firstname_input_element()
        return element.get_attribute('value')
    
    def get_lastname(self):
        element = self.__get_lastname_input_element()
        return element.get_attribute('value')
    
    def get_gender(self):
        element = self.__get_gender_element()
        return element.get_attribute('value')


    def get_address(self):
        element = self.__get_address_element()
        return element.get_attribute('value')
    
    def get_age(self):
        element = self.__get_age_element()
        return element.get_attribute('value')

    def get_phone(self):
        element = self.__get_phone_element()
        return element.get_attribute('value')

    def get_hobby(self):
        element = Select(self.__get_hobby_element())
        try:
            result = element.first_selected_option
            return result.text
        except NoSuchElementException:
            return ''
    
    def get_current_pwd(self):
        return self.__get_current_password_element().text
    
    def get_new_pwd(self):
        return self.__get_new_password_element().text
    
    def get_confirm_pwd(self):
        return self.__get_confirm_password_elemrnt().text
    
    def get_lang(self):
        element = Select(self.__get_lang_element())
        return element.first_selected_option.text
    
    def get_firstname_error(self):
        ElementState = namedtuple('firstname_msg',['text', 'is_displayed'])
        element = self.__get_firstname_err_msg()
        element_state = ElementState(element.text, element.is_displayed())
        return element_state
    
    def get_lastname_error(self):
        ElementState = namedtuple('lastname_msg',['text', 'is_displayed'])
        element = self.__get_lastname_err_msg()
        element_state = ElementState(element.text, element.is_displayed())
        return element_state

    def get_pwd_mismatch_error(self):
        ElementState = namedtuple('confirm_msg',['text', 'is_displayed'])
        element = self.__get_confirm_msg()
        element_state = ElementState(element.text, element.is_displayed())
        return element_state

    def check_sav_btn_status(self):
        element = self.__get_save_btn()
        return element.is_enabled()
    
    def check_login_uneditable(self):
        element = self.__get_loginname_input_element()
        return not element.is_enabled()

    def __get_firstname_err_msg(self):
        return self.browser.find_element(By.XPATH, self.REQUIRE_FN_MSG_XPATH)
    
    def __get_lastname_err_msg(self):
        return self.browser.find_element(By.XPATH, self.REQUIRE_LN_MSG_XPATH)

    def __get_success_info_element(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.SUCCESS_INFO_CSS)
    
    def __get_error_info_element(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.ERROR_INFO_CSS)

    def __get_loginname_input_element(self):
        return self.browser.find_element(By.ID, self.USERNAME_INPUT_ID)
    
    def __get_firstname_input_element(self):
        return self.browser.find_element(By.ID, self.FIRSTNAME_INPUT_ID)

    def __get_lastname_input_element(self):
        return self.browser.find_element(By.ID, self.LASTNAME_INPUT_ID)
    
    def __get_gender_element(self):
        return self.browser.find_element(By.ID, self.GENDER_ID)

    def __get_age_element(self):
        return self.browser.find_element(By.ID, self.AGE_ID)

    def __get_address_element(self):
        return self.browser.find_element(By.ID, self.ADDRESS_ID)

    def __get_phone_element(self):
        return self.browser.find_element(By.ID, self.PHONE_ID)

    def __get_hobby_element(self):
        return self.browser.find_element(By.ID, self.HOBBY_ID)

    def __get_current_password_element(self):
        return self.browser.find_element(By.ID, self.CURRENT_PASSWORD_ID)

    def __get_new_password_element(self):
        return self.browser.find_element(By.ID, self.NEW_PASSWORD_ID)

    def __get_confirm_password_elemrnt(self):
        return self.browser.find_element(By.ID, self.CONFIRM_PASSWORD_ID)

    def __get_lang_element(self):
        return self.browser.find_element(By.ID, self.LANG_ID)

    def __get_save_btn(self):
        return self.browser.find_element(By.XPATH, self.SAVE_BTN_XPATH)

    def __get_gender_opt(self, opt):
        return self.browser.find_element(By.XPATH, self.GENDER_OPTION_XPATH.format(opt))

    def __get_confirm_msg(self):
        return self.browser.find_element(By.XPATH, self.REQUIRE_CPW_MSG_XPATH)