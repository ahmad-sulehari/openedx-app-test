"""
What's New Test Module
"""

import pytest

from framework import expect
from framework.element import Element
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.common import values
from tests.common.enums.attributes import ElementAttribute
from tests.common.globals import Globals


@pytest.mark.ANDROID
@pytest.mark.SMOKE
class TestAndroidWhatsNew:
    """
    What's new screen's Test Case
    """

    def test_start_whats_new_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify What's New screen is loaded successfully
        """

        setup_logging.info(f"Starting {TestAndroidWhatsNew.__name__} Test Case")
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        android_sign_in = AndroidSignIn()
        global_contents = Globals(setup_logging)
        whats_new_page = AndroidWhatsNew()

        if whats_new_page.get_close_button.exists(raise_exception=False):
            expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
            assert android_landing.signin_button.exists()
            assert android_landing.load_signin_screen()
            expect(android_sign_in.signin_title, "Sign in screen not loaded successfully").to_have(values.SIGN_IN_TEXT)
            expect(android_sign_in.sign_in_email_label).to_have(values.EMAIL_OR_USERNAME)
            expect(android_sign_in.sign_in_tf_email).to_be_clickable()
            assert android_sign_in.sign_in_tf_email.send_keys(global_contents.login_user_name)
            expect(android_sign_in.sign_in_password_label).to_have(values.PASSWORD)
            expect(android_sign_in.sign_in_password_field).to_be_clickable()
            assert android_sign_in.sign_in_password_field.send_keys(global_contents.login_password)
            expect(android_sign_in.signin_button).to_be_clickable()
            assert android_sign_in.signin_button.click()
        else:
            setup_logging.info("Whats New feature is not enabled")

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify following contents are visible on screen
                "Screen Title", "Cross Icon", "Main Feature Image",
                    "Feature Title", "Feature Details", "Done"
            Verify all screen contents have their default values
        """

        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        whats_new_page = AndroidWhatsNew()

        if whats_new_page.get_close_button.exists(raise_exception=False):
            expect(whats_new_page.get_close_button).to_be_clickable()
            expect(android_landing.screen_title).to_have(values.WHATS_NEW_TITLE)
            assert whats_new_page.get_whats_new_msg_title.get_attribute(ElementAttribute.TEXT)
            assert whats_new_page.get_whats_new_description.get_attribute(ElementAttribute.TEXT)
            assert whats_new_page.next_btn.exists()

            expect(whats_new_page.navigate_features()).to_have("Done")
            assert whats_new_page.done_button.click()
        else:
            setup_logging.info("Whats New feature is not enabled")
