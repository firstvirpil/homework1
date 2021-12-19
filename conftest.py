import logging


class BaseTest:
    """BaseTest class for inheritance. Implements test class default variables."""
    # Defined to fix 'unresolved attribute' warning
    # Default values to provide autocomplite
    logger = logging.getLogger(__name__)
