from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObject:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def click_element(self, locator):
        self.get_element(locator).click()

    def send_keys(self, locator, text):
        self.get_element(locator).send_keys(text)