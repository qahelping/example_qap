from pages.main_page import MainPage


def test_main_page_opened(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.assert_that_main_is_opened()