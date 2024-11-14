from src.utils.selenium_utils import init_driver
from src.config.config import BROWSER, TEST_CASES


def run_test_suite():

    for test_case_name in TEST_CASES:
        driver = init_driver(BROWSER)
        module = __import__('src.tests', fromlist=[test_case_name])
        test_class = getattr(module, test_case_name)
        test_case = test_class.TestCase(driver)
        test_case.test_steps()
        driver.quit()


if __name__ == '__main__':
    run_test_suite()