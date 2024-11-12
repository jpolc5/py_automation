from h11 import SERVER

from src.models.page_object import PageObject
from src.config import config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class TestCase:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(config.BASE_URL)
        self.page_object = PageObject(driver)

    def test_case1(self):
        caja_busqueda = self.page_object.get_element('//textarea[@id="APjFqb"]')
        caja_busqueda.send_keys('uatx')
        caja_busqueda.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        uatx_element = self.page_object.get_element("//A[contains(@href, 'https://uatx.mx')]")
        uatx_element.click()
