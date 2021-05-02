from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class OverallPage:
    """ represent the overall page """

    TITLE_MAKE_XPATH = "//th[2]"
    TITLE_MODEL_XPATH = "//th[3]"
    TITLE_RANK_XPATH = "//th[4]"
    TITLE_VOTES_XPATH = "/th[5]"
    TITLE_ENGINES_XPATH = "/th[6]"

    CONTENT_PIC_XPATH = "//tr[{}]/td[1]/a"
    CONTENT_MAKE_XPATH = "//tr[{}]/td[2]/a"
    CONTENT_MODEL_XPATH = "//tr[{}]/td[3]/a"
    CONTENT_RANK_XPATH = "//tr[{}]/td[4]"
    CONTENT_VOTES_XPATH = "//tr[{}]/td[5]"
    CONTENT_ENGINES_XPATH = "//tr[{}]/td[6]"
    CONTENT_COMMENTS_XPATH = "//tr[{}]/td[7]"

    VIEWMORE_LINK_XPATH = "//tr[{}]/td[7]/a"

    def __init__(self, browser):
        self.browser = browser
    
    def goTo_model_by_pic(self, num):
        element = self.__get_content_pic(num)
        element.click()
    
    def goTo_model_by_modellink(self, num):
        element = self.__get_content_model(num)
        element.click()

    def goTo_make(self, num):
        element = self.__get_content_make(num)
        element.click()
    
    def use_viewMore(self, num):
        element = self.__get_viewmore(num)
        element.click()
    
    def sort_by_make_name(self):
        element = self.__get_title_make()
        element.click()
    
    def sort_by_model_name(self):
        element = self.__get_title_model()
        element.click()

    def sort_by_rank(self):
        element = self.__get_title_rank()
        element.click()

    def sort_by_votes(self):
        element = self.__get_title_votes()
        element.click()
    
    def sort_by_engines(self):
        element = self.__get_title_engines()
        element.click()

    def get_value_model(self, num):
        element =self.__get_content_model(num)
        return element.text
    
    def get_value_make(self, num):
        element =self.__get_content_make(num)
        return element.text

    def get_value_rank(self, num):
        element =self.__get_content_rank(num)
        return element.text

    def get_value_votes(self, num):
        element =self.__get_content_votes(num)
        return element.text
    
    def get_value_engine(self, num):
        element =self.__get_content_engines(num)
        return element.text

    def __get_title_make(self):
        return self.browser.find_element(By.XPATH, self.TITLE_MAKE_XPATH)

    def __get_title_model(self):
        return self.browser.find_element(By.XPATH, self.TITLE_MODEL_XPATH)

    def __get_title_rank(self):
        return self.browser.find_element(By.XPATH, self.TITLE_RANK_XPATH)

    def __get_title_votes(self):
        return self.browser.find_element(By.XPATH, self.TITLE_VOTES_XPATH)

    def __get_title_engines(self):
        return self.browser.find_element(By.XPATH, self.TITLE_ENGINES_XPATH)
    
    def __get_content_pic(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_PIC_XPATH.format(num))
        
    def __get_content_make(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_MAKE_XPATH.format(num))
        
    def __get_content_model(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_MODEL_XPATH.format(num))
    
    def __get_content_rank(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_RANK_XPATH.format(num))
    
    def __get_content_votes(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_VOTES_XPATH.format(num))

    def __get_content_engines(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_MAKE_XPATH.format(num))
    
    def __get_content_comments(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_COMMENTS_XPATH.format(num))

    def __get_viewmore(self, num):
        return self.browser.find_element(By.XPATH, self.VIEWMORE_LINK_XPATH.format(num))

    
    