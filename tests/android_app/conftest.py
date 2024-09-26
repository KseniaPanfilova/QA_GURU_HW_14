import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import project


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        'platformName': 'android',
        'platformVersion': '9.0',
        'deviceName': 'Google Pixel 3',

        # Set URL of the application under test
        'app': 'bs://sample.app',

        # Set other BrowserStack capabilities
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            # Set your access credentials
            'userName': project.config.userName,
            'accessKey': project.config.accessKey
        }
    })

    browser.config.driver_remote_url = project.config.remote_url
    browser.config.driver_options = options
    browser.config.timeout = project.config.timeout

    yield

    browser.quit()
