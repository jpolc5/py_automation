from src.models.page_object import PageObject
from src.config import config
from selenium.webdriver.common.keys import Keys


class TestCase:

    def __init__(self, driver):
        # set driver for firefox in config.py
        self.driver = driver
        #open firefox with the url in config.py variable BASE_URL for this example we use google main page
        self.driver.get(config.BASE_URL)
        # set page_object with the locator functions in  page_object.py
        self.driver.maximize_window()
        self.page_object = PageObject(driver)

    def test_steps(self):
        #start to find first element in google main page, text area search
        caja_busqueda = self.page_object.get_element('//textarea[@id="APjFqb"]')
        #in caja_busqueda typing 'uatx' word
        caja_busqueda.send_keys('uatx')
        # send a return or 'enter' keystroke
        caja_busqueda.send_keys(Keys.RETURN)
        # this is for an amount time necesary for page load info
        self.driver.implicitly_wait(10)
        uatx_element = self.page_object.get_element("//A[contains(@href, 'https://uatx.mx')]")
        uatx_element.click()

        menu_uatx = self.page_object.get_element("//a[@class='dropdown-toggle active' and text()='Admisión']")
        menu_uatx.click()
        lic_menu_uatx = self.page_object.get_element("//a[@href='/admision']")
        lic_menu_uatx.click()
        lic_compu_link = self.page_object.get_element("//a[@href='https://siia5.uatx.mx:8743/siia-aspirantes/#/registro']")
        lic_compu_link.click()
