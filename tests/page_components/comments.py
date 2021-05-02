from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from collections import namedtuple

class CommentComponent:
    """ represent CommentList Component"""

    TITLE_DATE_XPATH = '//thead/th[1]'
    TITLE_AUTHOR_XPATH = '//thead/th[2]'
    TITLE_COMMENT_XPATH = '//thead/th[3]'
    CONTENT_DATE_XPATH = '//tbody/tr[{}]/td[1]'
    CONTENT_AUTHOR_XPATH = '//tbody/tr[{}]/td[2]'
    CONTENT_COMMENT_XPATH = '//tbody/tr[{}]/td[3]'
    COUNT_COMMENTS_XPATH = '//tbody/tr'

    def __init__(self, browser):
        self.browser = browser
    
    def get_title(self):
        date_title = self.__get_title_of_date().text
        author_title = self.__get_title_of_author().text
        comment_title = self.__get_title_of_comment().text
        return (date_title, author_title, comment_title)
    
    def get_content(self, num):
        Content = namedtuple('content',['date', 'author', 'comment'])
        ele_date_content = self.__get_date_content(num)
        ele_author_content = self.__get_author_content(num)
        ele_comment_content = self.__get_comment_content(num)
        content = Content(ele_date_content.text, ele_author_content.text, ele_comment_content.text)
        return content

    def __get_date_content(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_DATE_XPATH.format(num))
    
    def __get_author_content(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_AUTHOR_XPATH.format(num))

    def __get_comment_content(self, num):
        return self.browser.find_element(By.XPATH, self.CONTENT_COMMENT_XPATH.format(num))

    def __get_title_of_date(self):
        return self.browser.find_element(By.XPATH, self.TITLE_DATE_XPATH)
    
    def __get_title_of_author(self):
        return self.browser.find_element(By.XPATH, self.TITLE_AUTHOR_XPATH)
    
    def __get_title_of_comment(self):
        return self.browser.find_element(By.XPATH, self.TITLE_COMMENT_XPATH)
    