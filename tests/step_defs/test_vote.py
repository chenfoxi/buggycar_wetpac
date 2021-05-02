import time
import pytest

from pytest_bdd import scenarios, given, when, then

from conf import Constants
from page_components.login import LoginPage
from page_components.home import HomePage
from page_components.register import RegisterPage
from page_components.vote import VoteComponent
from page_components.comments import CommentComponent
from utils.random_utils import get_random_string, get_random_password




# Scenarios

scenarios('vote.feature', features_base_dir=Constants.FEATURE_FILES_BASE_DIR)

# Fixtures
@pytest.fixture
def login_page(getBrowser):
    alogin = LoginPage(getBrowser)
    return alogin

@pytest.fixture
def home_page(getBrowser):
    aHome = HomePage(getBrowser)
    return aHome

@pytest.fixture
def register_page(getBrowser):
    aRegister = RegisterPage(getBrowser)
    return aRegister

@pytest.fixture
def vote_component(getBrowser):
    aVote = VoteComponent(getBrowser)
    return aVote

@pytest.fixture
def comment_component(getBrowser):
    aComment = CommentComponent(getBrowser)
    return aComment

@pytest.fixture
def random_username():
    user = {
        'name': '',
        'password': ''
    }
    yield user
    user['name'] = ''
    user['password'] = ''

# private method

# Given Steps

@given('Go to register page register a new user <username>')
def get_new_user(getBrowser, register_page, random_username, username):
    getBrowser.get(Constants.get_register_url())
    random_username['name'] = username + get_random_string(8)
    random_username['password'] = 'A!1' + get_random_password()
    register_page.register_all(random_username['name'], username, username, random_username['password'], random_username['password'])

@given('Login with the new user')
def login_with_new_user(login_page, random_username):
    time.sleep(1)
    login_page.login_with_usename(random_username['name'], random_username['password'])

@given('Go to a model')
def goTo_model(home_page):
    home_page.goTo_home()
    home_page.goTo_popular_model()

@given('Without login and go to a model')
def without_login_goto_model(getBrowser, home_page):
    getBrowser.get(Constants.get_buggycar_host())
    home_page.goTo_popular_model()


# When Steps

@when('the user add <comment> and vote')
def vote_and_add_comment(vote_component, comment):
    vote_component.vote(comment)

@when('the user vote')
def vote_without_comment(vote_component):
    vote_component.vote('')
    

@when('the user want to vote')
def want_vote():
    # dummy code
    pass

# Then Steps

@then('vote successfully')
def check_vote_successfully(vote_component):
    msg = vote_component.get_msg()
    assert msg == 'Thank you for your vote!'

@then('cannot vote')
def check_vote_status(vote_component):
    assert vote_component.can_vote() == False

@then('comment <comment> showed successfully')
def check_comment_content(comment_component, comment):
    actual_comment = comment_component.get_content(1)
    assert actual_comment.comment == comment