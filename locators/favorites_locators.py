from selenium.webdriver.common.by import By


class FavouritesLocators:
    FAVORITES = (By.CSS_SELECTOR, 'class="favourites"')
    GO_SHOPPING_BUTTON = (By.XPATH, '//*[@data-text="strGoShopping"]')
    EMPTY_PAGE = (By.CLASS_NAME, "favourites-empty")
    TITLE = (By.CSS_SELECTOR, 'data-text="strFavouritesEmptyTitle"')
