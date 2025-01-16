from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers.assertions import Assertions



class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

        self.assertions = Assertions(driver)

    def open_page(self, url):
        self.driver.get(url)

    def click(self, selector):
        element = self.wait_for(selector)
        element.click()

    def fill(self, selector, text):
        element = self.wait_for(selector)
        element.send_keys(text)
    
    def wait_for_title(self, text, time_out=10):
        return WebDriverWait(self.driver, time_out).until(
            EC.title_is(text)
        )
    
    def get_element(self, selector, time_out=10):
        return WebDriverWait(self.driver, time_out).until(
            EC.element_to_be_clickable(selector)
        )
    
    def wait_for(self, selector, time_out=10):
        try:
            return self.get_element(selector, time_out)
        except TimeoutException:
            assert False, f"Element {selector[1]} not found"

    def wait_for_disappear(self, selector, time_out=10):
        try:
            WebDriverWait(self.driver, time_out).until_not(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            assert False, f"Element {selector[1]} not found"

    def add_cookie(self, name, value):
        cookie = {"name": name, "value": value}
        self.driver.add_cookie(cookie)

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    def get_text(self, selector):
        element = self.driver.find_element(*selector)
        return element.text

    def scroll_to_element(self, selector):
        element = self.driver.find_element(*selector)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)

    def scroll_to_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    