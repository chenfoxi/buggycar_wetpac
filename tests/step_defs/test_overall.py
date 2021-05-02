import time
import pytest

from pytest_bdd import scenarios, given, when, then

from conf import Constants

from page_components.page import PageComponent
from page_components.overall import OverallPage




# Scenarios

scenarios('overall_rating.feature', features_base_dir=Constants.FEATURE_FILES_BASE_DIR)

# Fixtures

@pytest.fixture
def home_page(getBrowser):
    aHome = HomePage(getBrowser)
    return aHome

@pytest.fixture
def overall_page(getBrowser):
    aOverall = OverallPage(getBrowser)
    return aOverall

@pytest.fixture
def page_component(getBrowser):
    aPage = PageComponent(getBrowser)
    return aPage

# private method

# Given Steps

@given('Go to overall page')
def goTo_overall(getBrowser):
    getBrowser.get(Constants.get_overall_url())
    time.sleep(1)

# When Steps

@when('the user sort the list by rank (click it)')
def sort_by_rank(overall_page):
    overall_page.sort_by_rank()
    time.sleep(1)

@when('the user click the viewmore button to see the <num> model')
def viewmore(overall_page, num):
    overall_page.use_viewMore(num)
    
@when('the user check the overall list')
def view_overall_list():
    # dummy code
    pass

@when('the user click right arrow to see next page')
def goTo_next_page(page_component):
    page_component.click_right_arrow()

@when('the user click left arrow to previous page')
def goTo_prev_page(page_component):
    page_component.click_left_arrow()

@when('the user input <num> in the edit control')
def input_page_num(page_component, num):
    page_component.edit_page(num)

# Then Steps

@then('rating list showed correctly')
def check_list_successfully(overall_page):
    make = overall_page.get_value_make(1)
    assert make == 'Lamborghini'

@then('rating show according the rank ascending')
def check_rank_sort(overall_page):
    first_rank = overall_page.get_value_rank(1)
    second_rank = overall_page.get_value_rank(2)
    assert first_rank == '1'
    assert second_rank == '2'

@then('go to a model page')
def check_goTo_model_page(getBrowser):
    assert getBrowser.current_url.startswith(Constants.get_buggycar_host() + "model/")

@then('go to the next page')
def check_goTo_next_page(page_component):
    actual_msg = page_component.get_pag_msg()
    assert actual_msg == '« » page 2 of 5'

@then('go to the previous page')
def check_goTo_prev_page(page_component):
    actual_msg = page_component.get_pag_msg()
    assert actual_msg == '« » page 1 of 5'

@then('go to the <num> page')
def check_goTo_num_page(page_component, num):
    actual_msg = page_component.get_pag_msg()
    assert actual_msg == '« » page ' + num + ' of 5'
