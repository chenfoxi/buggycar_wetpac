from collections import namedtuple

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.selenium_utils import simulate_onChange


class RegisterPage:
    """ represent the register page """
    USERNAME_INPUT_ID = "username"
    FIRSTNAME_INPUT_ID = "firstName"
    LASTNAME_INPUT_ID = "lastName"
    PASSWORD_ID = "password"
    CONFIRM_PASSWORD_ID = "confirmPassword"
    REG_BTN_XPATH = "//button[text()='Register']"
    CANCEL_BTN_XPATH = "//a[text()='Cancel']"

    REQUIRE_LOGIN_MSG_XPATH = "//input[@id='username']/following-sibling::div[1]"
    REQUIRE_FN_MSG_XPATH = "//input[@id='firstName']/following-sibling::div[1]"
    REQUIRE_LN_MSG_XPATH = "//input[@id='lastName']/following-sibling::div[1]"
    REQUIRE_PW_MSG_XPATH = "//input[@id='password']/following-sibling::div[1]"
    REQUIRE_CPW_MSG_XPATH = "//input[@id='confirmPassword']/following-sibling::div[1]"

    SUCCESS_INFO_CSS = "[class='result alert alert-success']"
    ERROR_INFO_CSS = "[class='result alert alert-danger']"

    def __init__(self, browser):
        self.browser = browser

    def register_all(self, username, firstname, lastname, password, confirmpw):
        username_input = self.__get_loginname_input_element()
        firstname_input = self.__get_firstname_input_element()
        lastname_input = self.__get_lastname_input_element()
        password_input = self.__get_password_input_element()
        confirm_input = self.__get_confirm_input_element()
        register_btn = self.__get_register_btn()

        username_input.send_keys(username)
        firstname_input.send_keys(firstname)
        lastname_input.send_keys(lastname)
        password_input.send_keys(password)
        confirm_input.send_keys(confirmpw)
        register_btn.click()

    def get_success_info(self):
        element = self.__get_success_info_element()
        return element.text
    
    def get_error_info(self):
        element = self.__get_error_info_element()
        return element.text
    
    def check_success_info_display(self):
        element = self.__get_success_info_element()
        return element.is_displayed()

    def check_reg_btn_enabled(self):
        element = self.__get_register_btn()
        return element.is_enabled()

    def input_username(self, username):
        element = self.__get_loginname_input_element()
        element.send_keys(username)
    
    def input_firstname(self, firstname):
        element = self.__get_firstname_input_element()
        element.send_keys(firstname)

    def input_lastname(self, lastname):
        element = self.__get_lastname_input_element()
        element.send_keys(lastname)

    def input_password(self, password):
        element = self.__get_password_input_element()
        element.send_keys(password)

    def input_confirmpassword(self, password):
        element = self.__get_confirm_input_element()
        element.send_keys(password)
    


    def clear_username_input(self):
        element = self.__get_loginname_input_element()
        simulate_onChange(element)

    def clear_firstname_input(self):
        element = self.__get_firstname_input_element()
        simulate_onChange(element)
    
    def clear_lastname_input(self):
        element = self.__get_lastname_input_element()
        simulate_onChange(element)
    
    def clear_password_input(self):
        element = self.__get_password_input_element()
        simulate_onChange(element)

    def clear_confirm_input(self):
        element = self.__get_confirm_input_element()
        simulate_onChange(element)

    def get_confirm_error(self):
        ElementState = namedtuple('confirm_msg',['text', 'is_displayed'])
        element = self.__get_confirm_msg()
        element_state = ElementState(element.text, element.is_displayed())
        return element_state

    def get_username_error(self):
        ElementState = namedtuple('username_msg',['text', 'is_displayed'])
        element = self.__get_username_err_msg()
        element_state = ElementState(element.text, element.is_displayed())
        return element_state

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
    
    def get_password_error(self):
        ElementState = namedtuple('password_msg',['text', 'is_displayed'])
        element = self.__get_password_err_msg()
        element_state = ElementState(element.text, element.is_displayed())
        return element_state

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

    def __get_password_input_element(self):
        return self.browser.find_element(By.ID, self.PASSWORD_ID)
    
    def __get_confirm_input_element(self):
        return self.browser.find_element(By.ID, self.CONFIRM_PASSWORD_ID)

    def __get_register_btn(self):
        return self.browser.find_element(By.XPATH, self.REG_BTN_XPATH)

    def __get_cancel_btn(self):
        return self.browser.find_element(By.XPATH, self.CANCEL_BTN_XPATH)

    def __get_confirm_msg(self):
        return self.browser.find_element(By.XPATH, self.REQUIRE_CPW_MSG_XPATH)

    def __get_username_err_msg(self):
        return self.browser.find_element(By.XPATH, self.REQUIRE_LOGIN_MSG_XPATH)

    def __get_firstname_err_msg(self):
        return self.browser.find_element(By.XPATH, self.REQUIRE_FN_MSG_XPATH)
    
    def __get_lastname_err_msg(self):
        return self.browser.find_element(By.XPATH, self.REQUIRE_LN_MSG_XPATH)

    def __get_password_err_msg(self):
        return self.browser.find_element(By.XPATH, self.REQUIRE_PW_MSG_XPATH)
    
    

    