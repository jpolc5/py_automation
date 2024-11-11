from src.tests.test_case import TestCase
from src.utils.selenium_utils import init_driver
from src.config.config import BROWSER, HEADLESS, TEST_CASES


def run_test_suite():
    driver = init_driver(BROWSER, HEADLESS)
    test_cases = [TestCase(driver) for _ in range(len(TEST_CASES))]
    for test_case in test_cases:
        test_case.test_case1()
    driver.quit()


if __name__ == '__main__':
    run_test_suite()