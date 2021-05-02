from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utils.selenium_utils import simulate_onChange

class PageComponent:
    """ represent page Component"""

    ARROW_LEFT_XPATH = "//my-pager//a[1]"
    ARROW_RIGHT_XPATH = "//my-pager//a[2]"
    PAGER_EDIT_XPATH = "//my-pager//input"
    PAGER_MSG_XPATH = '//my-pager//div[@class="pull-xs-right"]'

    def __init__(self, browser):
        self.browser = browser

    def check_left_arrow_enable(self):
        element = self.__get_left_arrow()
        return element.is_enabled()
    
    def click_left_arrow(self):
        element = self.__get_left_arrow()
        element.click()

    def check_right_arrow_enable(self):
        element = self.__get_right_arrow()
        return element.is_enabled()
    
    def click_right_arrow(self):
        element = self.__get_right_arrow()
        element.click()
    
    def edit_page(self, num):
        element = self.__get_page_edit()
        ActionChains(self.browser).move_to_element(element).perform()
        simulate_onChange(element)
        element.send_keys(num)
        element.send_keys(Keys.ENTER)
    
    def get_pag_msg(self):
        return self.__get_pager_msg()

    def __get_left_arrow(self):
        return self.browser.find_element(By.XPATH, self.ARROW_LEFT_XPATH)
    
    def __get_right_arrow(self):
        return self.browser.find_element(By.XPATH, self.ARROW_RIGHT_XPATH)
    
    def __get_page_edit(self):
        return self.browser.find_element(By.XPATH, self.PAGER_EDIT_XPATH)
    
    def __get_pager_msg(self):
        return self.browser.find_element(By.XPATH, self.PAGER_MSG_XPATH).text
    