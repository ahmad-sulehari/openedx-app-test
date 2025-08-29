"""
Course Dashboard Screen Test Module
"""

import allure
import pytest

from framework import expect, Element
from tests.common.enums import ElementAttribute
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.common import values
from tests.ios.pages.ios_main_dashboard import IosMainDashboard


@allure.suite("IOS SMOKE")
@pytest.mark.IOS
@pytest.mark.IOS_SMOKE
class TestIosCourseDashboard:
    """
    Course Dashboard screen's Test Case
    """

    def test_validate_ui_elements(self, ios_login, setup_logging):
        """
        Scenarios:
            Verify that clicking course from Main dashboard load course dashboard,
            Verify that Course Dashboard tab will show following contents,
            Header contents,
                Back icon,
                Specific "<course name>" as Title, Share icon, Course,
            Verify on tapping "Videos" tab will load Videos screen
            Verify on tapping "Discussion" tab will load Discussions screen
            Verify on tapping "Dates" tab will load Dates screen
            Verify on tapping "Resources" tab will load Resources list
            Verify on tapping "Handouts" tab will load Handouts screen
            Verify on tapping "Announcements" tab will load Announcements screen
            Verify on tapping "Home" tab will load Home screen
        """
        driver = ios_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        course_dashboard_page = IosCourseDashboard()
        main_dashboard = IosMainDashboard()

        with allure.step("open course from learn tab by clicking on it"):
            course_dashboard_page.find_by_text_on_screen(values.MY_COURSES_SECOND_COURSE_NAME).click()

        with allure.step("dismiss notification popup if appears"):
            if course_dashboard_page.allow_notifications_button.exists(raise_exception=False):
                course_dashboard_page.allow_notifications_button.click()

        with allure.step("verify home tab is shown"):
            expect(course_dashboard_page.course_dashboard_home_tab).to_have(
                values.COURSE_DASHBOARD_HOME_TAB, ElementAttribute.LABEL
            )

        with allure.step("verify course name is shown"):
            course_dashboard_page.find_by_text_on_screen(values.DEMOX)

        with allure.step("verify video tab label and click on it"):
            videos_tab = course_dashboard_page.course_dashboard_videos_tab
            expect(videos_tab).to_have(values.COURSE_DASHBOARD_VIDEOS_TAB, ElementAttribute.LABEL)
            videos_tab.click()

        with allure.step("verify discussions tab label and click on it"):
            discussions_tab = course_dashboard_page.course_dashboard_discussions_tab
            expect(discussions_tab).to_have(values.COURSE_DASHBOARD_DISCUSSIONS_TAB, ElementAttribute.LABEL)
            discussions_tab.click()

        with allure.step("verify dates tab label and click on it"):
            dates_tab = course_dashboard_page.course_dashboard_dates_tab
            expect(dates_tab).to_have(values.COURSE_DASHBOARD_DATES_TAB, ElementAttribute.LABEL)
            dates_tab.click()

        with allure.step("verify more tab label and click on it"):
            more_tab = course_dashboard_page.course_dashboard_more_tab
            expect(more_tab).to_have(values.COURSE_DASHBOARD_MORE_TAB, ElementAttribute.LABEL)
            more_tab.click()

        with allure.step("click on go back button and verify main dashboard page"):
            dashboard_tab = course_dashboard_page.back_navigation_button
            expect(dashboard_tab).to_have(values.LANDING_BACK_BUTTON, ElementAttribute.LABEL)
            dashboard_tab.click()
            expect(main_dashboard.learn_tab).to_have(values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE)
