import pytest
from selenium import webdriver

@pytest.fixture()
def web(browser_request):
     if browser_request=='chrome':
        Openbrowser=webdriver.Chrome()
        print("chrome opening")
     elif browser_request =='firefox':
         Openbrowser = webdriver.Firefox()
     elif browser_request == 'ie':
        Openbrowser = webdriver.Ie()
     return Openbrowser

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser_request(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project name'] = 'NOP ecommerce'
    config._metadata['class'] = 'Automation with Selenium'
    config._metadata['tester'] = 'Ramya Mahesh'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)