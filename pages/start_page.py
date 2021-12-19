import logging

from selenium.webdriver.common.by import By

from constants import start_page_constants
from pages.base import BasePage
from pages.header import Header


class StartPage(BasePage):
    """Class store actions and verification related to start page """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)
        self.header = Header(driver)

    def fill_sign_in_fields(self, username, password):
        """ Fill specified fields using passed values"""
        # Click on Enter
        self.wait_until_click(locator_type=By.XPATH, locator=start_page_constants.SIGN_IN_BUTTON_ENTER_XPATH)
        self.logger.debug('Clicked on sign up')

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page_constants.SIGN_IN_LOGIN_FIELD_XPATH, data=username)
        self.logger.info("Set login value: '%s'", username)

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page_constants.SIGN_IN_PASSWORD_FIELD_XPATH, data=password)
        self.logger.debug("Set password value: '%s'", password)

        # Click on Sign In
        self.wait_until_click(locator_type=By.XPATH, locator=start_page_constants.SIGN_IN_BUTTON_SIGN_XPATH)
        self.logger.debug('Clicked on sign up')

    def verify_invalid_credentials(self):
        # Check error message on invalid credentials
        error_message = self.wait_until_find(locator_type=By.XPATH, locator=start_page_constants.INVALID_LOGIN_ERROR_XPATH)
        assert error_message.text == 'Error', f"Actual: {error_message.text}"
        self.logger.debug('Error message was verified')
