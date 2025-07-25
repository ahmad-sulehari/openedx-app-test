"""
Profile Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidProfile(AndroidBasePage):
    """
    Profile screen
    """

    def __init__(self):
        super().__init__()
        self._settings_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Settings")')
        self._profile_img_profile = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("img_profile")')
        self._profile_txt_name = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_profile_name")'
        )
        self._profile_username = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_profile_username")'
        )
        self._edit_profile_btn_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_edit_profile")'
        )
        self._privacy_policy = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Privacy Policy")')
        self._logout_text = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log out")')
        self._logout_prompt_msg = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_logout_dialog_title")'
        )
        self._prompt_logout_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_logout")')
        self._logout_prompt_logout_button_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_logout")'
        )
        self._logout_dialogue_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_logout_dialog_title")'
        )
        self._profile_screen_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_profile_title")'
        )
        self._profile_edit_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_edit")')
        self._profile_txt_settings = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings").instance(0)'
        )
        self._profile_txt_video_settings = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_video_settings")'
        )
        self._profile_txt_support_info = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Contact Support")'
        )

        self._profile_settings_password_input = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("tf_password_input")'
        )
        self._profile_settings_delete_account_confirm = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_yes,_delete_account")'
        )
        self._profile_settings_delete_account = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_delete_account")'
        )
        self._profile_settings_back_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Back")'
        )
        self._profile_settings_about_me = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("About Me")')
        self._profile_settings_about_me_body = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_profile_bio")'
        )
        self._edit_profile_btn = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_edit_profile")'
        )

    @property
    def profile_settings_about_me(self):
        """
        Getter for the about me element on the profile settings page.

        Returns:
            Element: The about me element.
        """
        return self._profile_settings_about_me

    @property
    def profile_settings_about_me_body(self):
        """
        Getter for the about me element on the profile settings page.

        Returns:
            Element: The about me element.
        """
        return self._profile_settings_about_me_body

    @property
    def profile_settings_back_button(self):
        """
        Getter for the back button element on the profile settings page.

        Returns:
            Element: The back button element.
        """
        return self._profile_settings_back_button

    @property
    def profile_settings_delete_account_confirm(self):
        """
        Getter for the confirm delete account button element on the profile settings page.

        Returns:
            Element: The confirm delete account button element.
        """
        return self._profile_settings_delete_account_confirm

    @property
    def profile_settings_password_input(self):
        """
        Getter for the password input element on the profile settings page.

        Returns:
            Element: The password input element.
        """
        return self._profile_settings_password_input

    @property
    def profile_settings_delete_account(self):
        """
        Getter for the 'Delete Account' element on the profile settings page.

        Returns:
            Element: The 'Delete Account' element.
        """
        return self._profile_settings_delete_account

    @property
    def logout_dialogue_title(self) -> Element:
        """
        Returns:
            Element: logout dialogue title element
        """

        return self._logout_dialogue_title

    def get_profile_edit_button(self) -> Element:
        """
        Returns:
            Element: profile edit button element
        """

        return self._profile_edit_button

    @property
    def profile_img_profile(self) -> Element:
        """
        Returns:
            Element: profile image element
        """

        return self._profile_img_profile

    @property
    def profile_txt_name(self) -> Element:
        """
        Returns:
            Element: profile text name element
        """

        return self._profile_txt_name

    @property
    def profile_username(self) -> Element:
        """
        Returns:
            Element: profile username element
        """

        return self._profile_username

    @property
    def get_profile_txt_settings(self) -> Element:
        """
        Returns:
            Element: profile settings element
        """

        return self._profile_txt_settings

    def get_profile_txt_video_settings(self) -> Element:
        """
        Returns:
            Element: profile video settings element
        """

        return self._profile_txt_video_settings

    @property
    def get_profile_txt_support_info(self):
        """
        Returns:
            Element: profile support info element
        """

        return self._profile_txt_support_info

    @property
    def get_profile_txt_contact_support(self) -> Element:
        """
        Returns:
            Element: profile contact support element
        """

        return self.find_by_text_on_screen(android_elements.profile_txt_contact_support)

    @property
    def get_profile_txt_terms_of_use(self) -> Element:
        """
        Returns:
            Element: profile terms of use element
        """

        return self.find_by_text_on_screen(android_elements.profile_txt_terms_of_use)

    @property
    def privacy_policy_text(self) -> Element:
        """
        Returns:
            Element: profile privacy policy element
        """

        return self._privacy_policy

    @property
    def get_profile_txt_cookie_policy(self) -> Element:
        """
        Returns:
            Element: profile cookie policy element
        """

        return self.find_by_text_on_screen(android_elements.profile_txt_cookie_policy)

    @property
    def get_profile_personal_info(self):
        """
        Returns:
            Element: profile personal info element
        """

        return self.find_by_text_on_screen(android_elements.profile_personal_info)

    @property
    def get_profile_txt_view_faq(self):
        """
        Returns:
            Element: profile view faq element
        """

        return self.find_by_text_on_screen(android_elements.profile_txt_view_faq)

    @property
    def get_profile_txt_up_to_date(self):
        """
        Returns:
            Element: profile up to date element
        """

        return self.find_by_text_on_screen(android_elements.profile_txt_up_to_date)

    @property
    def profile_txt_logout(self) -> Element:
        """
        Returns:
            Element: profile logout element
        """

        return self._logout_text

    @property
    def logout_prompt_msg(self) -> Element:
        """
        Returns:
            Element: profile logout element
        """

        return self._logout_prompt_msg

    @property
    def logout_prompt_logout_button_text(self) -> Element:
        """
        Returns:
            Element: logout button element
        """

        return self._logout_prompt_logout_button_text

    @property
    def logout_prompt_logout_button(self) -> Element:
        """
        Returns:
            Element: logout button element
        """

        return self._prompt_logout_button

    @property
    def settings_button(self) -> Element:
        """
        Returns:
            Element: settings button element
        """

        return self._settings_button

    @property
    def get_settings_screen_title(self):
        """
        Returns:
            Element: settings screen title element
        """

        return self.find_by_text_on_screen(android_elements.profile_settings_txt)

    @property
    def get_manage_account_label(self) -> Element:
        """
        Returns:
            Element: manage account label element
        """

        return self.find_by_text_on_screen(android_elements.profile_manage_account_label)

    @property
    def get_video_label(self) -> Element:
        """
        Returns:
            Element: video label element
        """

        return self.find_by_text_on_screen(android_elements.profile_video_label)

    def get_dates_calendar_label(self):
        """
        Returns:
            Element: Dates & Calendar label element
        """

        return self.find_by_text_on_screen(android_elements.profile_dates_calendar_label)

    @property
    def edit_profile_button_text(self) -> Element:
        """
        Returns:
            Element: edit profile button element
        """

        return self._edit_profile_btn_text

    @property
    def edit_profile_button(self) -> Element:
        """
        Returns:
            Element: edit profile button element
        """

        return self._edit_profile_btn
