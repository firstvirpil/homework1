import logging

from pages.base import BasePage


class Header(BasePage):
    """Store header actions and helpers """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)
