"""
    My Courses Test Module
"""

from selenium.webdriver.common.by import By
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.common import values
from tests.common.globals import Globals
from tests.conftest import android_login


class TestAndroidMyCoursesList:
    """
    My Courses screen's Test Case
    """

    def test_validate_ui_elements(self, android_login, setup_logging):
        """
         Scenarios:
            Verify that from Main Dashboard tapping Courses tab will load My Courses
            list(of specific logged-in user) in its tab
            Verify that Courses tab/screen will show following header contents,
            Header Contents
                Learn
            Verify that My Courses(enrolled) List with followings in each course,
                Progress bar
                Organization
                Name
                Start/End date
                Due date
                Resume label
                Second Course
                Third Course
            Verify that tapping any course should load specific Course Dashboard screen
            Verity that from Course Dashboard tapping back should load My Courses List screen
        """
        driver = android_login
        global_contents = Globals(setup_logging)
        main_dashboard_page = AndroidMainDashboard(driver, setup_logging)
        learn_tab = main_dashboard_page.get_learn_tab()
        assert learn_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_LEARN_TAB
        assert learn_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        course_view = global_contents.wait_and_get_element(driver, 'org.edx.mobile:id/view_pager')
        assert course_view.get_attribute('displayed') == values.TRUE_LOWERCASE
        progress_bar = global_contents.get_all_views_on_screen(driver, 'android.widget.ProgressBar')[0]
        assert progress_bar.text == '0.0'

        course_organization = course_view.find_elements(By.CLASS_NAME, 'android.widget.TextView')[2]
        assert course_organization.text == values.MAIN_DASHBOARD_COURSE_ORG
        course_name = course_view.find_elements(By.CLASS_NAME, 'android.widget.TextView')[3]
        assert course_name.text == values.MAIN_DASHBOARD_COURSE_NAME
        course_end_date = course_view.find_elements(By.CLASS_NAME, 'android.widget.TextView')[4]
        assert course_end_date.text
        due_date = course_view.find_elements(By.CLASS_NAME, 'android.widget.TextView')[5]
        assert due_date.text
        resume_label = course_view.find_elements(By.CLASS_NAME, 'android.widget.TextView')[6]
        assert resume_label.text == values.MAIN_DASHBOARD_RESUME_LABEL
        resume_content = course_view.find_elements(By.CLASS_NAME, 'android.widget.TextView')[7]
        assert resume_content.text
        view_all_courses_label = course_view.find_elements(By.CLASS_NAME, 'android.widget.TextView')[8]
        assert values.MAIN_DASHBOARD_ALL_COURSES_LABEL in view_all_courses_label.text
        second_course_name = course_view.find_elements(By.CLASS_NAME, 'android.widget.TextView')[9]
        assert second_course_name.text == values.MY_COURSES_SECOND_COURSE_NAME
        third_course_name = course_view.find_elements(By.CLASS_NAME, 'android.widget.TextView')[10]
        assert third_course_name.text

    def test_view_all_courses(self, android_login, setup_logging):
        """
        Scenarios:
            Verify that tapping View All My Courses label should load My Courses List screen
            Verify All Courses  label should be displayed
            Verify that tapping All label should load all enrolled courses
            Verify that tapping In Progress label should load all in progress courses
            Verify that tapping Completed label should load all completed courses
            Verify that tapping Expired label should load all expired courses
            Verify that tapping back button should load Main Dashboard screen
        """
        driver = android_login
        global_contents = Globals(setup_logging)

        course_view = global_contents.wait_and_get_element(driver, 'org.edx.mobile:id/view_pager')
        view_all_courses_label = course_view.find_elements(By.CLASS_NAME, 'android.widget.TextView')[8]
        assert values.MAIN_DASHBOARD_ALL_COURSES_LABEL in view_all_courses_label.text
        view_all_courses_label.click()

        all_courses_label = global_contents.get_element_by_text(driver, 'All Courses')
        assert all_courses_label.text == values.MY_COURSES_ALL_COURSES_LABEL

        all_courses = global_contents.get_element_by_text(driver, 'All')
        assert all_courses.text == values.MY_COURSES_ALL_COURSES_LABEL
        all_courses.click()

        all_enrolled_courses = global_contents.get_all_views_on_screen(driver, 'android.widget.ProgressBar')
        assert len(all_enrolled_courses) == 3

        in_progress = global_contents.get_element_by_text(driver, 'In Progress')
        assert in_progress.text == values.MY_COURSES_IN_PROGRESS_LABEL
        in_progress.click()
        assert len(all_enrolled_courses) == 3

        completed = global_contents.get_element_by_text(driver, 'Completed')
        assert completed.text == values.MY_COURSES_COMPLETED_LABEL
        completed.click()

        global_contents.wait_for_element_visibility(driver, 'txt_empty_state_title')
        assert global_contents.wait_and_get_element(
            driver, 'txt_empty_state_title').text == 'No Completed Courses'

        assert global_contents.wait_and_get_element(
            driver, 'txt_empty_state_title').text == 'No Completed Courses'

        expired = global_contents.get_element_by_text(driver, 'Expired')
        assert expired.text == values.MY_COURSES_EXPIRED_LABEL
        expired.click()

        global_contents.wait_for_element_visibility(driver, 'How to Learn Online')
        assert global_contents.get_android_element_by_text(
            driver, 'How to Learn Online').text == 'How to Learn Online'

        assert global_contents.wait_and_get_element(
            driver, 'txt_empty_state_title').text == 'No Expired Courses'

        assert global_contents.get_back_button(driver)
        global_contents.get_back_button(driver).click()
