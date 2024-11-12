from selenium import webdriver


def init_driver(browser):
    if browser == 'chrome':
        return webdriver.Chrome()
    elif browser == 'firefox':
        return webdriver.Firefox()
