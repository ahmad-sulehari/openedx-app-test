"""Test Module for Course Switcher in iOS Learn Tab"""

import allure
import pytest

from framework import expect
from framework.element import Element
from tests.common.enums.attributes import ElementAttribute
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList


@allure.epic("IOS SMOKE")
@allure.feature("Course Switcher")
@allure.story("user can switch between courses and programs")
@allure.suite("IOS SMOKE")
@pytest.mark.IOS
@pytest.mark.IOS_SMOKE
class TestIosCourseSwitcher:
    """
    Test class for validating course switcher functionality in iOS Learn tab.
    """

    def test_validate_programs_switcher(self, ios_login, setup_logging):
        """
        Scenarios:
           Verify following contents are visible on screen,
               Courses switcher
               Profile Tab, Programs Tab, Profiel tab
           Verify that clicking courses switcher will open dropdown
           Verify that dropdown has courses and programs options in it
           Verify that clicking each menu will load its screen
        """
        driver = ios_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        main_dashboard = IosMainDashboard()
        my_courses_list = IosMyCoursesList()

        main_dashboard.learn_tab.click()
        expect(my_courses_list.courses_dropdown_menu).to_have("Courses", ElementAttribute.LABEL)
        my_courses_list.courses_dropdown_menu.click()
        expect(my_courses_list.courses_option).to_have("Courses", ElementAttribute.LABEL)
        expect(my_courses_list.programs_option).to_have("Programs", ElementAttribute.LABEL)
        my_courses_list.courses_option.click()
        expect(my_courses_list.courses_dropdown_menu).to_have("Courses", ElementAttribute.LABEL)
        my_courses_list.courses_dropdown_menu.click()
        my_courses_list.programs_option.click()
        expect(my_courses_list.courses_dropdown_menu).to_have("Programs", ElementAttribute.LABEL)
        my_courses_list.courses_dropdown_menu.click()
        my_courses_list.courses_option.click()
        expect(my_courses_list.courses_dropdown_menu).to_have("Courses", ElementAttribute.LABEL)
