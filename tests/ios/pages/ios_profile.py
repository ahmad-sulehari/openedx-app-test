"""
    Profile Page Module
"""
from appium.webdriver.common.appiumby import AppiumBy

from framework import Element
from tests.ios.pages.ios_base_page import IosBasePage


class IosProfile(IosBasePage):
    """
    Profile screen
    """

    def __init__(self):
        super().__init__()
        self._profile_screen_title = Element(AppiumBy.NAME, 'Profile')
        self._profile_edit_button = Element(AppiumBy.ACCESSIBILITY_ID, 'edit_profile_button')
        self._profile_settings_button = Element(AppiumBy.ACCESSIBILITY_ID, 'settings')
        self._profile_user_avatar_image = Element(AppiumBy.ACCESSIBILITY_ID, 'user_avatar_image')
        self._profile_user_name_text = Element(AppiumBy.ACCESSIBILITY_ID, 'user_name_text')
        self._profile_user_username_text = Element(AppiumBy.ACCESSIBILITY_ID, 'user_username_text')
        self._profile_settings_text = Element(AppiumBy.ACCESSIBILITY_ID, 'settings_text')
        self._profile_logout_button = Element(AppiumBy.ACCESSIBILITY_ID, 'logout_button')
        self._profile_logout_dialogue_title = Element(AppiumBy.NAME, 'Are you sure you want to log out?')
        self._profile_logout_close_button = Element(AppiumBy.NAME, 'xmark')
        self._profile_logout_confirmation = Element(AppiumBy.ACCESSIBILITY_ID, 'logout_confirmation')
        self._profile_logout_confirmation_button = Element(AppiumBy.ACCESSIBILITY_ID, 'logout_confirmation_button')
        self._profile_video_settings_button = Element(AppiumBy.ACCESSIBILITY_ID, 'video_settings_button')
        self._profile_manage_account_label = Element(AppiumBy.ACCESSIBILITY_ID, 'Manage Account')
        self._profile_dates_calendar_label = Element(AppiumBy.ACCESSIBILITY_ID, 'Dates & Calendar')
        self._profile_support_info_text = Element(AppiumBy.ACCESSIBILITY_ID, 'support_info_text')
        self._profile_tos_text = Element(AppiumBy.NAME, 'tos')
        self._manage_account_text = Element(AppiumBy.ACCESSIBILITY_ID, 'manage_account_text')
        self._main_dashboard_profile_tab = Element(AppiumBy.ACCESSIBILITY_ID, 'Profile')
        self._arrow_left_back_button = Element(AppiumBy.ACCESSIBILITY_ID, 'arrowLeft')
        self._version_info = Element(AppiumBy.ACCESSIBILITY_ID, 'version_info')
        self._profile_view_faq = Element(AppiumBy.ACCESSIBILITY_ID, 'view_faq')
        self._profile_contact_support = Element(AppiumBy.ACCESSIBILITY_ID, 'Contact support')
        self._profile_dont_sell_data = Element(AppiumBy.ACCESSIBILITY_ID, 'dont_sell_data')
        self._profile_cookies_policy = Element(AppiumBy.ACCESSIBILITY_ID, 'cookies_policy')
        self._profile_privacy_policy = Element(AppiumBy.ACCESSIBILITY_ID, 'privacy_policy')
        self._edit_profile_title = Element(AppiumBy.IOS_PREDICATE, 'name CONTAINS "Edit profile"')


    @property
    def edit_profile_title(self) -> Element:
        """"""

        return self._edit_profile_title

    @property
    def get_profile_screen_title(self) -> Element:
        """
        Get profile screen title

        Returns:
            webdriver element: Profile screen title element
        """

        return self._profile_screen_title

    @property
    def get_profile_edit_button(self) -> Element:
        """
        Get profile edit button

        Returns:
            webdriver element: Profile edit button element
        """

        return self._profile_edit_button

    @property
    def profile_settings_button(self) -> Element:
        """
        Get profile settings button

        Returns:
            webdriver element: Profile settings button element
        """

        return self._profile_settings_button

    @property
    def profile_img_profile(self) -> Element:
        """
        Get profile image

        Returns:
            webdriver element: Profile image element
        """

        return self._profile_user_avatar_image

    @property
    def profile_user_name_text(self) -> Element:
        """
        Get user's name text

        Returns:
            webdriver element: User's name text element
        """

        return self._profile_user_name_text

    @property
    def profile_user_username_text(self) -> Element:
        """
        Get user's username text

        Returns:
            webdriver element: User's username text element
        """

        return self._profile_user_username_text

    @property
    def get_profile_settings_text(self) -> Element:
        """
        Get settings text

        Returns:
            webdriver element: Settings text element
        """

        return self._profile_settings_text

    @property
    def get_profile_video_settings_button(self) -> Element:
        """
        Get video settings button

        Returns:
            webdriver element: Video settings button element
        """

        return self._profile_video_settings_button.find_all()[1]

    @property
    def get_profile_manage_account_label(self) -> Element:
        """
        Get manage account label

        Returns:
            webdriver element: Manage account label element
        """

        return self._profile_manage_account_label

    @property
    def get_profile_dates_calendar_label(self) -> Element:
        """
        Get dates calendar label

        Returns:
            webdriver element: Dates & Calendar element
        """

        return self._profile_dates_calendar_label

    @property
    def get_profile_support_info_text(self) -> Element:
        """
        Get support info text

        Returns:
            webdriver element: Support info text element
        """

        return self._profile_support_info_text

    @property
    def get_profile_tos_text(self) -> Element:
        """
        Get tos text

        Returns:
            webdriver element: Tos text element
        """

        return self._profile_tos_text

    @property
    def get_profile_privacy_policy(self) -> Element:
        """
        Get privacy policy

        Returns:
            webdriver element: Privacy policy element
        """

        return self._profile_privacy_policy

    @property
    def get_profile_cookies_policy(self) -> Element:
        """
        Get cookies policy

        Returns:
            webdriver element: Cookies policy element
        """

        return self._profile_cookies_policy

    @property
    def get_profile_dont_sell_data(self) -> Element:
        """
        Get dont sell data

        Returns:
            webdriver element: Dont sell data element
        """

        return self._profile_dont_sell_data

    @property
    def get_profile_contact_support(self) -> Element:
        """
        Get contact support

        Returns:
            webdriver element: Contact support element
        """

        return self._profile_contact_support

    @property
    def get_profile_view_faq(self) -> Element:
        """
        Get view faq

        Returns:
            webdriver element: View faq element
        """

        return self._profile_view_faq

    @property
    def get_profile_version_info(self) -> Element:
        """
        Get version info

        Returns:
            webdriver element: Version info element
        """

        return self._version_info

    @property
    def get_profile_logout_button(self) -> Element:
        """
        Get logout button

        Returns:
            webdriver element: Logout button element
        """

        return self._profile_logout_button

    @property
    def get_logout_close_button(self) -> Element:
        """
        Get close button

        Returns:
            webdriver element: Close button element
        """

        return self._profile_logout_close_button

    @property
    def get_logout_dialog_title(self) -> Element:
        """
        Get dialog title

        Returns:
            webdriver element: Dialog title element
        """

        return self._profile_logout_dialogue_title

    @property
    def get_logout_button(self) -> Element:
        """
        Get logout button

        Returns:
            webdriver element: Logout button element
        """

        return self._profile_logout_button

    @property
    def get_back_button(self) -> Element:
        """
        Get discovery title

        Returns:
            webdriver element: discovery title element
        """

        return self._arrow_left_back_button

    @property
    def get_videos_back_button(self) -> Element:
        """
        Get videos settings page

        Returns:
            webdriver element: back element
        """

        return self._main_dashboard_profile_tab

    @property
    def get_manage_account_title(self) -> Element:
        """
        Returns:
            element: manage account title element
        """

        return self._manage_account_text
