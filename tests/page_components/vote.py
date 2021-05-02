from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class VoteComponent:
    """ represent Vote Component"""

    COMMENT_TEXTAREA_ID = 'comment'
    VOTE_BTN_XPATH = "//button[text()='Vote!']"
    MSG_XPATH = "//p[@class='card-text']"

    def __init__(self, browser):
        self.browser = browser

    def can_vote(self):
        try:
            self.__get_comment()
            return True
        except NoSuchElementException:
            return False
        
    def vote(self, comment):
        comment_element = self.__get_comment()
        comment_element.send_keys(comment)
        vote_btn = self.__get_vote_btn()
        vote_btn.click()

    def get_msg(self):
        element = self.__get_msg()
        return element.text

    def __get_comment(self):
        return self.browser.find_element(By.ID, self.COMMENT_TEXTAREA_ID)
    
    def __get_vote_btn(self):
        return self.browser.find_element(By.XPATH, self.VOTE_BTN_XPATH)
    
    def __get_msg(self):
        return self.browser.find_element(By.XPATH, self.MSG_XPATH)