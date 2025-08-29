"""
Course Home Tab Screen Test Module
"""

import allure
import pytest

from framework import expect, Element
from tests.common.enums import ElementAttribute
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.common import values
from tests.ios.pages.ios_course_home_tab import IosCourseHomeTab


@allure.suite("IOS SMOKE")
@pytest.mark.IOS
@pytest.mark.IOS_SMOKE
class TestIosCourseHomeTab:
    """
    Course Home Tab screen's Test Case
    """

    def test_validate_ui_elements(self, ios_login, setup_logging):
        """
        Scenarios:
            Verify that clicking course from Main dashboard load course dashboard,
            Verify that Course Dashboard tab will show following contents,
            Header contents,
                Back icon,
                Specific "<course name>" as Title, Share icon, Course,
            Verify course deadline title and description
            Verify shift due dates button
            Verify continue with label
            Verify resume button
            Verify introduction section
            Verify subsection element
            Verify clicking subsection element will load component screen
            Verify component header title
            Verify back button
            Verify section element
            Verify second subsection element
            Verify clicking second subsection element will load component screen
            Verify homework element
            Verify second component header
            Verify back button
        """
        driver = ios_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        course_dashboard_page = IosCourseDashboard()

        with allure.step("open course from learn tab by clicking on it"):
            course_dashboard_page.find_by_text_on_screen(values.MY_COURSES_SECOND_COURSE_NAME).click()

        with allure.step("dismiss notification popup if appears"):
            if course_dashboard_page.allow_notifications_button.exists(raise_exception=False):
                course_dashboard_page.allow_notifications_button.click()

        course_tab = course_dashboard_page.course_dashboard_home_tab
        expect(course_tab).to_have(values.COURSE_DASHBOARD_HOME_TAB, ElementAttribute.LABEL)

        course_dashboard_page.find_by_text_on_screen(values.COURSE_MISSED_DEADLINES_LABEL)

        course_dashboard_page.find_by_text_on_screen(values.COURSE_DEADLINE_DESCRIPTION_LABEL)

        course_dashboard_page.find_by_text_on_screen(values.COURSE_SHIFT_DUE_DATES)

        course_dashboard_page.find_by_text_on_screen(values.COURSE_RESUME_WITH_LABEL)

        course_dashboard_page.find_by_text_on_screen(values.COURSE_RESUME_BUTTON)

        Element.swipe_vertical_full_page()
        introduction_section = course_dashboard_page.find_by_text_on_screen(values.COURSE_SECTION_LABEL)
        introduction_section.click()

        subsection_elem = course_dashboard_page.find_by_text_on_screen(values.COURSE_INTRO_MODULE_SUBSECTION_LABEL)
        subsection_elem.click()

        course_dashboard_page.find_by_text_on_screen(values.COURSE_INTRO_MODULE_SUBSECTION_LABEL)
        course_dashboard_page.progress_bar.wait_to_disappear()
        course_dashboard_page.back_navigation_button.click()
        course_dashboard_page.progress_bar.wait_to_disappear()
        Element.swipe_vertical_full_page()
        section1_elem = course_dashboard_page.find_by_text_on_screen(values.COURSE_SECTION_1_LABEL)
        section1_elem.click()

        course_dashboard_page.find_by_text_on_screen(values.COURSE_SUBSECTION_1_LABEL)

        homework_elem = course_dashboard_page.find_by_text_on_screen(values.COURSE_SUBSECTION_HOMEWORK1_LABEL)
        homework_elem.click()

        course_dashboard_page.find_by_text_on_screen(values.COURSE_SUBSECTION_HOMEWORK1_LABEL)

    def test_component_navigation_smoke(self, ios_login, setup_logging):
        """
        Scenarios:
            Verify next button element, and it is clickable
            Verify previous button element, and it is clickable
            Verify user can click on next button until finish button appears
            Verify clicking finish button will load the celebratory modal
            Verify Back to outline button on Modal and clicking this button
                loads the components screen
            Verify clicking on back button will navigate the user to dashboard page
        """
        driver = ios_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        course_home_page = IosCourseHomeTab()

        next_btn = course_home_page.next_btn
        expect(next_btn).to_have(values.COURSE_COMPONENT_NEXT_BUTTON, ElementAttribute.LABEL)
        next_btn.click()

        prev_btn = course_home_page.prev_btn
        expect(prev_btn).to_have(values.COURSE_COMPONENT_PREVIOUS_BUTTON, ElementAttribute.LABEL)
        prev_btn.click()

        finish_button = course_home_page.component_navigation()
        expect(finish_button).to_have(values.COURSE_COMPONENT_FINISH_BUTTON, ElementAttribute.LABEL)
        finish_button.click()

        back_to_outline = course_home_page.find_by_text_on_screen(values.COURSE_COMPLETION_BACK_BUTTON)
        back_to_outline.click()

        back_btn = course_home_page.back_button
        expect(back_btn).to_have(values.LANDING_BACK_BUTTON, ElementAttribute.LABEL)
        back_btn.click()
