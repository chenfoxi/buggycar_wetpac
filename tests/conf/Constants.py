
def get_buggycar_host():

    HOST = 'https://buggy.justtestit.org/'
    return HOST

def get_register_url():
    return get_buggycar_host() + 'register'

def get_overall_url():
    return get_buggycar_host() + 'overall'

XPATH_CLASS_HELPER = "contains(concat(' ',normalize-space(@class),' '),'{}')"

FEATURE_FILES_BASE_DIR = 'tests/features'
