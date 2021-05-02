from selenium.webdriver.common.by import By

class LoginPage:
    """ represent the login page """
    USERNAME_INPUT_NAME = "login"
    PASSWORD_INPUT_NAME = "password"
    LOGIN_BTN_XPATH = "//button[contains(text(),'Login')]"

    FAILED_MSG_CSS = "[class='label label-warning']"

    NAME_LABEL_XPATH = "//ul/li[1]/span"
    PROFILE_LABEL_XPATH = "//ul/li[2]/a"
    LOGOUT_XPATH = "//ul/li[3]/a"

    HOME_LINK_CSS = "[class='navbar-brand']"

    def __init__(self, browser):
        self.browser = browser

    def login_with_usename(self, username, password):
        username_input = self.browser.find_element(By.NAME, self.USERNAME_INPUT_NAME)
        password_input = self.browser.find_element(By.NAME, self.PASSWORD_INPUT_NAME)
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit = self.browser.find_element(By.XPATH, self.LOGIN_BTN_XPATH)
        submit.click()
        

    def get_login_failed_msg(self):
        error_msg_ele = self.browser.find_element(By.CSS_SELECTOR, self.FAILED_MSG_CSS)
        return error_msg_ele.text

    def logout(self):
        logout_btn = self.browser.find_element(By.XPATH, self.LOGOUT_XPATH)
        logout_btn.click()
    
    def get_login_name(self):
        login_name = self.browser.find_element(By.XPATH, self.NAME_LABEL_XPATH)
        return login_name.text

    def check_login(self):
        return len(self.browser.find_elements(By.XPATH, self.NAME_LABEL_XPATH)) == 1
    
    def check_logout(self):
        elements = self.browser.find_elements(By.XPATH, self.NAME_LABEL_XPATH)
        return len(elements) == 0
    
    def check_login_elements(self):
        username_input = self.browser.find_elements(By.NAME, self.USERNAME_INPUT_NAME)
        password_input = self.browser.find_elements(By.NAME, self.PASSWORD_INPUT_NAME)
        login_btn = self.browser.find_elements(By.XPATH, self.LOGIN_BTN_XPATH)
        return len(username_input) == 1 and len(password_input) == 1 and len(login_btn) == 1
    
    def get_profile_link(self):
        return self.browser.find_element(By.XPATH, self.PROFILE_LABEL_XPATH)

    def get_browser(self):
        return self.browser

    def goto_profile(self):
        self.browser.find_element(By.XPATH, self.PROFILE_LABEL_XPATH).click()
    
    def return_home_page(self):
        home_link = self.browser.find_element(By.CSS_SELECTOR, self.HOME_LINK_CSS)
        home_link.click()