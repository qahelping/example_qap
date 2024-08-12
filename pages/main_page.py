from data.urls import BASE_URL
from elements import HeaderElement
from pages import BasePage
from selenium.webdriver.common.by import By


class MainLocators:
    HEADER = (By.CSS_SELECTOR, '[class="header"]')
    SLIDER = (By.XPATH, '//*[@class="slider"]')
    RECOMMENDATIONS = (By.CLASS_NAME, "recommendations")


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainLocators

    def open(self):
        self.open_page(BASE_URL)

    def assert_that_main_is_opened(self):
        assert self.get_element(self.locators.HEADER)
        assert self.get_element(self.locators.SLIDER)
        assert self.get_element(self.locators.RECOMMENDATIONS)
