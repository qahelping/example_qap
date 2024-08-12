from data.urls import BASE_URL
from elements import HeaderElement
from locators import FavouritesLocators
from pages import BasePage


class FavouritesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = FavouritesLocators

    def open(self):
        self.open_page(BASE_URL)

    def assert_that_page_is_opened(self):
        assert self.get_element(self.locators.FAVORITES)
        assert self.get_element(self.locators.GO_SHOPPING_BUTTON)
        assert self.get_element(self.locators.EMPTY_PAGE)

        self.assertions.assert_that_text_is_visible(self.locators.TITLE, 'Здесь будут избранные товары')
