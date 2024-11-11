from src.models.page_object import PageObject


class TestCase:
    def __init__(self, driver):
        self.driver = driver
        self.page_object = PageObject(driver)

    def test_case1(self):
        self.page_object.get_element('//input[@id="username"]').send_keys('username')
        self.page_object.get_element('//input[@id="password"]').send_keys('password')
        self.page_object.click_element('//button[@id="login"]')
        assert self.page_object.get_element('//h1[@id="welcome"]').text == 'Welcome!'