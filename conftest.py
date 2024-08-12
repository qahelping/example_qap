import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options

# from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import pytest


# def pytest_addoption(parser):
#     parser.addoption("--browser",
#                      action="store",
#                      default="chrome",
#                      help="Run tests with different configuration of browser")
#
#     parser.addoption("--headless",
#                      action="store",
#                      default="true",
#                      help="Run tests with incognito mode")


# def run_chrome_driver(headless):
    # options = webdriver.ChromeOptions()
    # if headless:
    #     options = webdriver.ChromeOptions()
    #     options.add_argument('--headless')
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    # driver.implicitly_wait(5)
    # driver.maximize_window()
    #
    # yield driver
    #
    # driver.close()
    # driver.quit()
#
#
# def run_firefox_driver(headless):
#     options = Options()
#     if headless:
#         options.add_argument('--headless')
#     driver = webdriver.Chrome(service=FirefoxService(GeckoDriverManager().install()), options=options)
#     driver.implicitly_wait(5)
#     driver.maximize_window()
#
#     yield driver
#
#     driver.close()
#     driver.quit()

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--window-size=1920,1080')
    options.add_argument("--disable-search-engine-choice-screen")
    chrome_install = ChromeDriverManager().install()
    folder = os.path.dirname(chrome_install)
    chromedriver_path = os.path.join(folder, "chromedriver.exe")
    chrome_service = ChromeService(chromedriver_path)
    driver = webdriver.Chrome(service=chrome_service, options=options)
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver

    # driver.close()
    driver.quit()

# Run tests with different configuration of browser
# @pytest.fixture(autouse=False, scope="function")
# def driver(request):
#     # browser = request.config.getoption("--browser")
#     # headless = request.config.getoption("--headless")
#     # if browser == "firefox":
#     #     run_firefox_driver(headless)
#     # else:
#     #     run_chrome_driver(headless)
#
#     options = webdriver.ChromeOptions()
#     if True:
#         options = webdriver.ChromeOptions()
#         options.add_argument('--headless')
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.implicitly_wait(5)
#     driver.maximize_window()
#
#     yield driver
#
#     driver.close()
#     driver.quit()
