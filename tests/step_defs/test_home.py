import pytest

from pytest_bdd import scenarios, given, when, then
from conf import Constants
from page_components.login import LoginPage
from page_components.home import HomePage 



# Scenarios

scenarios('home.feature', features_base_dir=Constants.FEATURE_FILES_BASE_DIR)

# Fixtures
@pytest.fixture
def login_page(getBrowser):
    alogin = LoginPage(getBrowser)
    return alogin

@pytest.fixture
def home_page(getBrowser):
    aHome = HomePage(getBrowser)
    return aHome

# private method
    
# Given Steps

@given('Go to Home page')
def get_home(getBrowser):
    getBrowser.get(Constants.get_buggycar_host())

# When Steps

@when('the user click popular make link')
def go_make(home_page):
    home_page.goTo_popular_make()

@when('the user click popular model link')
def go_model(home_page):
    home_page.goTo_popular_model()

@when('the user click overall link')
def go_overall_rating(home_page):
    home_page.goTo_overall_rating()

# Then Steps

@then('ckick home logo can go back')
def go_back_home(getBrowser, home_page):
    home_page.goTo_home()
    assert getBrowser.current_url == Constants.get_buggycar_host()

@then('successfully go to make page')
def check_goto_make_page(getBrowser):
    assert getBrowser.current_url.startswith(Constants.get_buggycar_host() + "make/")
    
@then('successfully go to model page')
def check_goto_model_page(getBrowser):
    assert getBrowser.current_url.startswith(Constants.get_buggycar_host() + "model/")

@then('successfully go to overall rating page')
def check_goto_overall_rating_page(getBrowser):
    assert getBrowser.current_url.startswith(Constants.get_buggycar_host() + "overall")