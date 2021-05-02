from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class ModelPage:
    """ represent the model page """

    MAKE_LINK_XPATH = '//div[@class="card-block text-xs-center"][1]/a'
    MAKE_TITLE_XPATH = '//div[@class="card-block text-xs-center"][2]/h4'

    MODEL_PIC_XPATH = '//div[@class="col-lg-6"]/div/a'
    SPEC_ENGINE_XPATH = '//div[@class="col-lg-4"]//ul/li[1]'
    SPEC_MAX_SPEED_XPATH = '//div[@class="col-lg-4"]//ul/li[2]'

    MODEL_NAME_XPATH = '//div[@class="row"]//h3'

    def __init__(self, browser):
        self.browser = browser
    
    def check_make_exist(self):
        try:
            self.__get_make_link()
            return True
        except NoSuchElementException:
            return False
    
    def goTo_make(self):
        element = self.__get_make_link()
        element.click()

    def get_make_title(self):
        return self.__get_make_title().text
    
    def get_engine_info(self):
        element = self.__get_spec_engine()
        return element.text
    
    def get_speed_info(self):
        element = self.__get_spec_speed()
        return element.text

    def __get_make_link(self):
        return self.browser.find_element(By.XPATH, self.MAKE_LINK_XPATH)
    
    def __get_make_title(self):
        return self.browser.find_element(By.XPATH, self.MAKE_TITLE_XPATH)
    
    def __get_model_pic(self):
        return self.browser.find_element(By.XPATH, self.MODEL_PIC_XPATH)
    
    def __get_spec_engine(self):
        return self.browser.find_element(By.XPATH, self.SPEC_ENGINE_XPATH)

    def __get_spec_speed(self):
        return self.browser.find_element(By.XPATH, self.SPEC_MAX_SPEED_XPATH)
    

    