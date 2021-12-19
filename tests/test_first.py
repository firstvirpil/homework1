import pytest
from selenium import webdriver

from conftest import BaseTest
from constants import start_page_constants as start_page_constants
from pages.start_page import StartPage


class TestStartPage(BaseTest):
    @pytest.fixture(scope='function')
    def start_page(self):
        driver = webdriver.Chrome(executable_path='drivers/chromedriver')
        driver.implicitly_wait(time_to_wait=5)
        # Open start page
        driver.get(start_page_constants.START_PAGE_URL)
        start_page = StartPage(driver)
        yield start_page
        driver.close()

    def test_empty_fields_login(self, start_page):
        """
        - Open start page
        - Click button Enter
        - Clear password and login fields
        - Click on Sign In
        - Verify error message
        """

        # Clear password and login fields
        start_page.fill_sign_in_fields(username="", password="")

        # Verify error message
        start_page.verify_invalid_credentials()

    def test_invalid_credentials(self, start_page):
        """
        - Open start page
        - Clear login and password fields
        - Set invalid values for login and password
        - Click on Sign in
        - Verify error message
        """

        # Clear login and password fields
        start_page.fill_sign_in_fields(username="Login123", password="Pwd147")

        # Verify error message
        start_page.verify_invalid_credentials()
