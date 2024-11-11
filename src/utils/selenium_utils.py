from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def init_driver(browser, headless):
    if browser == 'chrome':
        options = Options()
        options.headless = headless
        return webdriver.Chrome(options=options)
    elif browser == 'firefox':
        # Implementar para Firefox
        pass