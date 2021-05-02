
from selenium.webdriver.common.by import By

class HomePage:
    """ represent home page"""
    
    POPULAR_MAKE_XPATH = "//h2[text()='Popular Make']/following-sibling::a[1]"
    POPULAR_MODEL_XPATH = "//h2[text()='Popular Model']/following-sibling::a[1]"
    TOTAL_RATING_XPATH = "//h2[text()='Overall Rating']/following-sibling::a[1]"
    HOME_LOGO_CSS = '[class="navbar-brand"]'

    def __init__(self, browser):
        self.browser = browser

    def goTo_popular_make(self):
        element = self.__get_popular_make_link()
        element.click()

    def goTo_popular_model(self):
        element = self.__get_popular_model_link()
        element.click()

    def goTo_overall_rating(self):
        element = self.__get_overall_rating_link()
        element.click()
    
    def goTo_home(self):
        element = self.__get_home_link()
        element.click()

    def __get_popular_make_link(self):
        return self.browser.find_element(By.XPATH, self.POPULAR_MAKE_XPATH)
    
    def __get_popular_model_link(self):
        return self.browser.find_element(By.XPATH, self.POPULAR_MODEL_XPATH)
    
    def __get_overall_rating_link(self):
        return self.browser.find_element(By.XPATH, self.TOTAL_RATING_XPATH)
    
    def __get_home_link(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.HOME_LOGO_CSS)