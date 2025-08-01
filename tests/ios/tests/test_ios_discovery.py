"""
Discovery Screen Test Module
"""

import pytest

from framework import expect, Element
from tests.common.enums import ElementAttribute

from time import sleep
from tests.common import values
from tests.common.globals import Globals
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_whats_new import IosWhatsNew


@pytest.mark.IOS
class TestIosDiscovery:
    """
    Discovery screen's Test Case
    """

    def test_start_discovery_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify discovery screen is loaded successfully
            Verify that the screen title is correct
            Verify that the explore courses button is displayed
            Verify that the explore courses button text is correct
            Verify that the back button is displayed
            Verify that the back button text is correct
            Verify that the discovery screen message is correct
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        setup_logging.info(f"Starting {TestIosDiscovery.__name__} Test Case")
        ios_landing = IosLanding()
        global_contents = Globals(setup_logging)

        logo_image = ios_landing.edx_logo_image
        expect(logo_image).to_have(values.LANDING_LOGO_IMAGE)

        expect(ios_landing.explore_all_courses_button).to_have(values.LANDING_EXLPORE_COURSES)
        ios_landing.explore_all_courses_button.click()
        expect(ios_landing.discover_page_back_button).to_have(values.BACK_BUTTON)
        assert (
            global_contents.get_element_by_label_ios(set_capabilities, "Discover").text
            == values.DISCOVER_SCREEN_HEADING
        )

        sleep(20)
        global_contents.wait_for_element_visibility(set_capabilities, values.DISCOVERY_SCREEN_MESSAGE)
        discovery_message = global_contents.wait_and_get_element(set_capabilities, "Build skills. Earn a certificate.")
        assert discovery_message.get_attribute("label") in values.DISCOVERY_SCREEN_MESSAGE

        chat_bot_close_btn = global_contents.wait_and_get_element(set_capabilities, "Close proactive message")
        assert chat_bot_close_btn.text == "Close proactive message"
        chat_bot_close_btn.click()

    def test_discovery_search_and_trending(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify search field is displayed
            Verify search field hint text
            Verify search button is displayed
            Verify search button text
            Verify trending label is displayed
            Verify trending label text
            Verify python course is displayed
            Verify python course text
            Verify excel course is displayed
            Verify excel course text
            Verify data course is displayed
            Verify data course text
            Verify marketing course is displayed
            Verify marketing course text
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        global_contents = Globals(setup_logging)

        search_field = global_contents.get_all_views_on_ios_screen(
            set_capabilities, ios_elements.discovery_search_field
        )[0]
        assert search_field.get_attribute("value") == values.DISCOVERY_SEARCH_FIELD_HINT

        search_button = global_contents.wait_and_get_element(set_capabilities, ios_elements.discovery_search_button)
        assert search_button.text == values.DISCOVERY_SEARCH_BUTTON

        trending_label = global_contents.get_element_by_name_ios(set_capabilities, values.DISCOVERY_TRENDING_LABEL_IOS)
        assert trending_label.get_attribute("name") == values.DISCOVERY_TRENDING_LABEL_IOS

        python_label = global_contents.get_element_by_label_ios(
            set_capabilities, values.DISCOVERY_TRENDING_COURSE_PYTHON
        )
        assert python_label.get_attribute("name") == values.DISCOVERY_TRENDING_COURSE_PYTHON

        excel_label = global_contents.get_element_by_label_ios(set_capabilities, values.DISCOVERY_TRENDING_COURSE_EXCEL)
        assert excel_label.get_attribute("name") == values.DISCOVERY_TRENDING_COURSE_EXCEL

        data_label = global_contents.get_element_by_label_ios(set_capabilities, values.DISCOVERY_TRENDING_COURSE_DATA)
        assert data_label.get_attribute("name") == values.DISCOVERY_TRENDING_COURSE_DATA

        marketing_label = global_contents.get_element_by_label_ios(
            set_capabilities, values.DISCOVERY_TRENDING_COURSE_MARKETING
        )
        assert marketing_label.get_attribute("name") == values.DISCOVERY_TRENDING_COURSE_MARKETING

    def test_discovery_popular_subjects(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify main content is displayed
            Verify main content text
            Verify search breadcrumb is displayed
            Verify search breadcrumb text
            Verify filter by popular courses is displayed
            Verify filter by popular courses text
            Verify first popular course is displayed
            Verify first popular course text
            Verify second popular course is displayed
            Verify second popular course text
            Verify third popular course is displayed
            Verify third popular course text
            Verify third popular course is clicked
            Verify results number is displayed
            Verify results number text
            Verify show results number is displayed
            Verify show results number text
            Verify show results number is clicked
            Verify pagination results is displayed
            Verify pagination results text
            Verify pagination text is displayed
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        global_contents = Globals(setup_logging)

        bread_crum = global_contents.wait_and_get_element(set_capabilities, values.DISCOVERY_SEARCH_BREADCRUMB_IOS)
        assert bread_crum.text == values.DISCOVERY_SEARCH_BREADCRUMB_IOS

        popular_courses = global_contents.get_element_by_name_ios(
            set_capabilities, values.DISCOVERY_FILTER_BY_POPULAR_COURSES
        )
        assert popular_courses.get_attribute("name") == values.DISCOVERY_FILTER_BY_POPULAR_COURSES

        search_field = global_contents.get_all_views_on_ios_screen(
            set_capabilities, ios_elements.discovery_search_field
        )[0]
        assert search_field.get_attribute("value") == values.DISCOVERY_SEARCH_FIELD_HINT

        global_contents.scroll_screen(set_capabilities, popular_courses, search_field)

        first_popular_course = global_contents.get_element_by_name_ios(
            set_capabilities, values.DISCOVERY_FIRST_POPULAR_COURSE
        )
        assert first_popular_course.get_attribute("name") == values.DISCOVERY_FIRST_POPULAR_COURSE

        second_popular_course = global_contents.get_element_by_name_ios(
            set_capabilities, values.DISCOVERY_SECOND_POPULAR_COURSE
        )
        assert second_popular_course.get_attribute("name") == values.DISCOVERY_SECOND_POPULAR_COURSE

        global_contents.scroll_screen(set_capabilities, second_popular_course, first_popular_course)

        math_course = global_contents.get_element_by_name_ios(set_capabilities, values.DISCOVERY_POPULAR_MATH_COURSE)
        assert math_course.get_attribute("name") == values.DISCOVERY_POPULAR_MATH_COURSE
        math_course.click()
        sleep(10)
        results_number = global_contents.get_element_by_name_ios(set_capabilities, values.DISCOVERY_MATH_RESULTS)
        assert results_number.get_attribute("name") == values.DISCOVERY_MATH_RESULTS
        sleep(5)
        show_results_number = global_contents.get_element_by_name_ios(
            set_capabilities, values.DISCOVERY_MATH_RESULTS_BUTTON
        )
        assert show_results_number.get_attribute("name") == values.DISCOVERY_MATH_RESULTS_BUTTON
        show_results_number.click()
        pagination_results = global_contents.get_element_by_name_ios(
            set_capabilities, values.DISCOVERY_MATH_PAGINATION_RESULTS
        )
        assert pagination_results.get_attribute("name") == values.DISCOVERY_MATH_PAGINATION_RESULTS
        pagination_text = global_contents.get_element_by_name_ios(
            set_capabilities, values.DISCOVERY_PAGINATION_TEXT_IOS
        )
        assert pagination_text.text == values.DISCOVERY_PAGINATION_TEXT_IOS

    def test_login_from_discovery(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that the user is able to login from discovery screen
            Verify that the user is able to navigate to the discover tab
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        global_contents = Globals(setup_logging)
        ios_login = IosLogin()
        ios_landing = IosLanding()
        whats_new_page = IosWhatsNew()

        signin_button = ios_landing.sign_in_button
        expect(signin_button).to_have(values.SIGN_IN_TEXT)
        assert signin_button.click()

        expect(ios_login.username_text_field_placeholder).to_have(values.EMAIL_OR_USERNAME_IOS)
        assert ios_login.username_textfield.send_keys(global_contents.login_user_name + "\n")

        expect(ios_login.password_text_field_label).to_have(values.PASSWORD)
        ios_login.password_textfield.send_keys(global_contents.login_password + "\n")
        sign_in_button = ios_login.signin_button
        expect(ios_login.signin_button).to_have(values.SIGN_IN_TEXT)
        sign_in_button.click()
        setup_logging.info(f"{global_contents.login_user_name} is successfully logged in")

        if whats_new_page.whats_new_next_button.exists(raise_exception=False):
            whats_new_page.close_button.click()

    def test_enroll_course_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify discover tab is loaded successfully
            Verify that the back button text is correct
            Verify that the discovery screen message is correct
            Verify that the search field is displayed
            Verify that the search field hint text is correct
            Verify that the search field is clickable
            Verify that the search field is filled with text
            Verify that the search result is displayed
            Verify that the search result text is correct
            Verify that the search result is clickable
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        global_contents = Globals(setup_logging)
        main_dashboard = IosMainDashboard()

        discover_tab = main_dashboard.main_dashboard_discover_tab
        assert discover_tab.click()
        expect(discover_tab).to_have(values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE)

        sleep(20)
        assert (
            global_contents.get_element_by_label_ios(set_capabilities, "Discover").text
            == values.DISCOVER_SCREEN_HEADING
        )

        discovery_message = global_contents.wait_and_get_element(set_capabilities, "Build skills. Earn a certificate.")
        assert discovery_message.get_attribute("label") in values.DISCOVERY_SCREEN_MESSAGE

        search_field = global_contents.get_all_views_on_ios_screen(
            set_capabilities, ios_elements.discovery_search_field
        )[0]
        assert search_field.get_attribute("value") == values.DISCOVERY_SEARCH_FIELD_HINT
        search_field.click()
        search_field.send_keys("Demo X")

        sleep(5)
        search_button = global_contents.wait_and_get_element(set_capabilities, ios_elements.discovery_search_button)
        assert search_button.text == values.DISCOVERY_SEARCH_BUTTON
        search_button.click()

    def test_search_course_in_discovery(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that the enrollment page is loaded successfully
            Verify that the enrollment date is displayed
            Verify that the enrollment date is clickable
            Verify that the enroll button is displayed
            Verify that the enroll button text is correct
            Verify that the enroll button is clickable
            Verify that the allow notifications button is displayed
            Verify that the allow notifications button text is correct
            Verify that the allow notifications button is clickable
            Verify that the home tab is displayed
            Verify that the home tab text is correct
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        global_contents = Globals(setup_logging)
        course_dashboard_page = IosCourseDashboard()

        sleep(5)
        global_contents.wait_for_element_visibility(set_capabilities, "logo for edX")
        edx_course_logo = global_contents.wait_and_get_element(set_capabilities, "logo for edX")
        assert edx_course_logo.get_attribute("name") == "logo for edX"
        edx_course_logo.click()

        sleep(20)
        session_available = global_contents.get_element_by_name_ios(set_capabilities, "There is one session available:")
        assert session_available.get_attribute("name") == "There is one session available:"

        enroll_button = global_contents.get_elements_by_name_ios(set_capabilities, "Enroll")[1]
        assert enroll_button.get_attribute("name") == "Enroll"
        assert enroll_button.get_attribute("value") == "Enroll"
        enroll_button.click()
        home_tab = course_dashboard_page.course_dashboard_course_tab
        expect(home_tab).to_have(values.COURSE_DASHBOARD_HOME_TAB)
