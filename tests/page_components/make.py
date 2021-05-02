from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MakePage:
    """ represent the make page """

    TITLE_MODEL_XPATH = "//th[2]"
    TITLE_RANK_XPATH = "//th[3]"
    TITLE_VOTES_XPATH = "/th[4]"

    CONTENT_PIC_XPATH = "//tr[{}]/td[1]/a"
    CONTENT_MODEL_XPATH = "//tr[{}]/td[2]/a"
    CONTENT_RANK_XPATH = "//tr[{}]/td[3]"
    CONTENT_VOTES_XPATH = "//tr[{}]/td[4]"
    CONTENT_COMMENTS_XPATH = "//tr[{}]/td[5]"

    VIEWMORE_LINK_XPATH = "//tr[{}]/td[5]/a"

    def __init__(self, browser):
        self.browser = browser
    
    def goTo_model_by_pic(self, num):
        element = self.__get_content_pic(num)
        element.click()
    
    def goTo_model_by_modellink(self, num):
        element = self.__get_content_model(num)
        element.click()
    
    def use_viewMore(self, num):
        element = self.__get_viewmore(num)
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

    def get_value_model(self, num):
        element =self.__get_content_model(num)
        return element.text
    
    def get_value_rank(self, num):
        element =self.__get_content_rank(num)
        return element.text

    def get_value_votes(self, num):
        element =self.__get_content_votes(num)
        return element.text

    def __get_title_model(self):
        return self.browser.find_element(By.XPATH, self.TITLE_MODEL_XPATH)

    def __get_title_rank(self):
        return self.browser.find_element(By.XPATH, self.TITLE_RANK_XPATH)

    def __get_title_votes(self):
        return self.browser.find_element(By.XPATH, self.TITLE_VOTES_XPATH)
    
    def __get_content_pic(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_PIC_XPATH.format(num))
        
    def __get_content_model(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_MODEL_XPATH.format(num))
    
    def __get_content_rank(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_RANK_XPATH.format(num))
    
    def __get_content_votes(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_VOTES_XPATH.format(num))
    
    def __get_content_comments(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_COMMENTS_XPATH.format(num))

    def __get_viewmore(self, num):
        return self.browser.find_element(By.XPATH, self.VIEWMORE_LINK_XPATH.format(num))


    