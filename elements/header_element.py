from pages import BasePage
from selenium.webdriver.common.by import By


class HeaderLocators:
    LIKED = (By.CSS_SELECTOR, '[class~="user-menu__item--heart-thin"]')


class HeaderElement(BasePage, HeaderLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_liked(self):
        self.click(self.LIKED)