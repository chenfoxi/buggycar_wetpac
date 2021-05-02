from selenium.webdriver.common.keys import Keys

def simulate_onChange(element):
    # for angular or react framework
    # to trigger the onChange action
    length = len(element.get_attribute('value'))
    element.send_keys(length * Keys.BACKSPACE)

def check_info_and_display(state, errormsg, is_displayed):
    # check namedtuple (text, is_displayed)
    assert state.text == errormsg
    assert state.is_displayed == is_displayed