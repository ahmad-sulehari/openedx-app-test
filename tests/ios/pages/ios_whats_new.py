"""
What's New Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element
from tests.common.enums import ElementAttribute
from tests.ios.pages.ios_base_page import IosBasePage


class IosWhatsNew(IosBasePage):
    """
    What's New screen
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IosWhatsNew, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self._close_button = Element(AppiumBy.NAME, "close_button")
        self._whats_new_next_button = Element(AppiumBy.ACCESSIBILITY_ID, "next_button")
        self._whats_new_msg_title = Element(AppiumBy.ACCESSIBILITY_ID, "title_text")
        self._whats_new_description = Element(AppiumBy.ACCESSIBILITY_ID, "description_text")
        self._whats_new_close_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'close_button'`]"
        )

    @property
    def whats_new_next_button(self) -> Element:
        """
        Get the 'What's New' next button element.

        Returns:
            Element: The next button element.
        """
        return self._whats_new_next_button

    @property
    def close_button(self) -> Element:
        """
        Get close button

        Returns:
            webdriver element: close Element
        """

        return self._whats_new_close_button

    @property
    def get_whats_new_msg_title(self) -> Element:
        """
        Get Whats New message title

        Returns:
            webdriver element: Whats New message title element
        """

        return self._whats_new_msg_title

    @property
    def get_whats_new_description(self) -> Element:
        """
        Get Whats New description

        Returns:
            webdriver element: Whats New description element
        """

        return self._whats_new_description

    def navigate_features(self):
        """
        Navigate between features

        Returns:
            webdriver element: Done Element
        """

        self.whats_new_next_button.click()

        if self.whats_new_next_button.get_attribute(ElementAttribute.LABEL) == "Done":
            return self.whats_new_next_button
        else:
            self.navigate_features()
            return self.whats_new_next_button
