"""Discover/Catalog Page Module."""

from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage
from tests.common import values
from appium.webdriver.common.appiumby import AppiumBy


class AndroidCatalogPage(AndroidBasePage):
    """A Class for handling Catalog Screen UI interactions."""

    def __init__(self):
        super().__init__()
        self._catalog_screen_toolbar_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_toolbar_title")'
        )
        self._catalog_screen_heading_msg = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Build skills. Earn a certificate. Advance your career.")',
        )
        self._trending_marketing_tag = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Marketing")')
        self._trending_python_tag = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Python")')
        self._trending_label = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Trending:")')
        self._trending_excel_tag = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Excel")')
        self._trending_data_science = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Data Sciences")')
        self._search_field = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            (
                'new UiSelector().resourceId("search-landing-search-input")'
                '.childSelector(new UiSelector().className("android.widget.EditText"))'
            ),
        )
        self._search_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("search-landing-search-submit")',
        )
        self._first_result = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("search-landing-product-result-0")',
        )
        self._discovery_enroll_main_element = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("enroll")',
        )
        self._enroll_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Enroll")')
        self._advance_your_career_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Advance your career")'
        )
        self._main_content = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("main-content")')
        self._course_start_date_text = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Starts")')
        self._course_end_date_text = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Ends")')
        self._discovery_search_breakcrumbs = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("breadcrumb")'
        )
        self._first_popular_course = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("subject-filter-0")',
        )
        self._second_popular_course = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("subject-filter-1")',
        )
        self._third_popular_course = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("subject-filter-2")',
        )
        self._course_carousel = Element(
            AppiumBy.XPATH,
            '//android.view.View[@resource-id="main-content"]/android.view.View[4]',
        )
        self._edx_demox_course_logo = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("header image for edX logo for edX DemoX edX Course")',
        )
        self._all_filters_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("All filters")')
        self._search_field = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("main-search-search-input")'
        )
        self._search_submit_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("main-search-search-submit")'
        )
        self._trending_tags = {
            values.DISCOVERY_TRENDING_COURSE_PYTHON: self._trending_python_tag,
            values.DISCOVERY_TRENDING_COURSE_MARKETING: self._trending_marketing_tag,
            values.DISCOVERY_TRENDING_LABEL: self._trending_label,
            values.DISCOVERY_TRENDING_COURSE_EXCEL: self._trending_excel_tag,
            values.DISCOVERY_TRENDING_COURSE_DATA: self._trending_data_science,
        }

    @property
    def course_carousel(self) -> Element:
        """course carousel
        Returns:
            Element: course carousel

        """
        return self._course_carousel

    @property
    def demox_course_logo_desc(self) -> Element:
        """course carousel
        Returns:
            Element: course carousel

        """
        return self._edx_demox_course_logo

    @property
    def main_content(self) -> Element:
        """Main content
        Returns:
            Element: main content
        """
        return self._main_content

    @property
    def discovery_search_breakcrumbs(self) -> Element:
        """Discovery search breakcrumbs
        Returns:
            Element: discovery search breakcrumbs

        """
        return self._discovery_search_breakcrumbs

    @property
    def first_popular_course(self) -> Element:
        """First popular course

        Returns:
            Element: first popular course

        """
        return self._first_popular_course

    @property
    def second_popular_course(self) -> Element:
        """Second popular course

        Returns:
            Element: second popular course

        """
        return self._second_popular_course

    @property
    def third_popular_course(self) -> Element:
        """Third popular course
        Returns:
            Element: third popular course
        """
        return self._third_popular_course

    @property
    def catalog_screen_toolbar_title(self) -> Element:
        """
        catalog screen toolbar title
        """
        return self._catalog_screen_toolbar_title

    @property
    def catalog_screen_heading_msg(self) -> Element:
        """catalog screen heading message
        Returns:
            Element: catalog screen heading message
        """

        return self._catalog_screen_heading_msg

    def trending_tag(self, tag: str) -> Element:
        """catalog screen trending marketing tag
        Returns:
            Element: catalog screen trending marketing tag
        """

        return self._trending_tags.get(tag)

    @property
    def search_field(self) -> Element:
        """Search field
        Returns:
            Element: search field

        """
        return self._search_field

    @property
    def search_button(self) -> Element:
        """Search button
        Returns:
            Element: search button

        """
        return self._search_button

    @property
    def first_result(self) -> Element:
        """First result
        Returns:
            Element: first result

        """
        return self._first_result

    @property
    def discovery_enroll_main_element(self) -> Element:
        """discovery enroll main element
        Returns:
            Element: discovery enroll main element

        """
        return self._discovery_enroll_main_element

    @property
    def course_start_date(self) -> Element:
        """course start date text view element
        Returns:
            Element: course start date text view element
        """
        return self._course_start_date_text

    @property
    def course_end_date(self) -> Element:
        """course end date text view element
        Returns:
            Element: course end date text view element

        """
        return self._course_end_date_text

    @property
    def enroll_button(self) -> Element:
        """Enroll button
        Returns:
            Element: enroll button
        """
        return self._enroll_button

    @property
    def all_filters_button(self) -> Element:
        """all filters button
        Returns:
            Element: all filters button

        """
        return self._all_filters_button

    @property
    def search_bar_text(self):
        """search bar text element
        Returns:
            Element: search bar text element
        """
        return self._search_field.get_child_element(self.edit_text_view)

    @property
    def advance_your_career_button(self):
        """Advance your career button
        Returns:
            Element: advance your career button
        """
        return self._advance_your_career_button
