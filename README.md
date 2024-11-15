Here is the updated `README.md` file with the `requirements.txt` file added:

**README.md**

PySelenium Framework
=====================

A Python-based automation framework using Selenium for web application testing.

Table of Contents
-----------------

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Creating Test Cases](#creating-test-cases)
6. [Running Test Suite](#running-test-suite)
7. [Troubleshooting](#troubleshooting)
8. [Contributing](#contributing)
9. [License](#license)

Introduction
------------

PySelenium is a lightweight and flexible automation framework designed to simplify web application testing using Selenium and Python. This framework provides a structured approach to creating and executing test cases, making it easy to maintain and extend your test suite.

Prerequisites
-------------

* Python 3.6+
* Selenium WebDriver (Chrome or Firefox)
* pip (Python package manager)

Installation
------------

1. Clone the repository: `git clone https://github.com/jpolc5/py_automation`
2. Install dependencies: `pip install -r requirements.txt`

Configuration
-------------

1. Update `config.py` with your environment variables:
	* `BASE_URL`: the base URL of the web application
	* `BROWSER`: the browser to use for testing (Chrome or Firefox)
2. Create a `test_suite.py` file to define your test suite

Creating Test Cases
-------------------

1. Create a new file in the `tests` directory (e.g., `test_login.py`)
2. Import the `LoginPage` class from `page_object.py`
3. Define a test case class that inherits from `LoginTestCase`
4. Implement test methods using the `LoginPage` class

Example:
```python
from page_object import LoginPage

class LoginTestCase:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def test_login(self):
        self.login_page.enter_username('username')
        self.login_page.enter_password('password')
        self.login_page.click_login()
        assert self.driver.title == 'Dashboard'
```

Running Test Suite
------------------

1. Run the test suite: `python test_suite.py`
2. The framework will execute the test cases in sequence and report any failures or errors

Troubleshooting
---------------

* Check the `logs` directory for error logs
* Verify that the `config.py` file is correctly configured
* Ensure that the Selenium WebDriver is properly installed and configured

Contributing
------------

* Fork the repository and create a new branch for your changes
* Submit a pull request with a clear description of your changes
* Ensure that your changes are tested and do not break existing functionality

License
-------

PySelenium is licensed under the GNU GENERAL PUBLIC LICENSE, Version 3.

**requirements.txt**

```
selenium==3.141.0
python==3.9.5
pip==21.1.2
setuptools==57.0.0
wheel==0.36.2
```

Note: The versions of the dependencies may vary depending on your specific use case and environment. The above versions are just examples.

You can generate the `requirements.txt` file automatically by running the following command in your terminal:
```
pip freeze > requirements.txt
```
This will list all the packages that are currently installed in your Python environment, along with their versions, and save them to a file named `requirements.txt`.

Alternatively, you can specify the dependencies manually by adding the package names and versions to the `requirements.txt` file. For example:
```
selenium
python
pip
setuptools
wheel
```
You can also specify the versions of the dependencies by adding the `==` symbol followed by the version number. For example:
```
selenium==3.141.0
python==3.9.5
pip==21.1.2
setuptools==57.0.0
wheel==0.36.2
```
Once you have created the `requirements.txt` file, you can install the dependencies by running the following command:
```
pip install -r requirements.txt
```
This will install all the dependencies listed in the `requirements.txt` file.
