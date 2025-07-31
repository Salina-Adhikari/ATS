from selenium import webdriver
import pytest
@pytest.fixture
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser=="Firefox":
        driver=webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver=webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):# this will  return the browser value to the setup method
    return request.config.getoption("--browser")
# It is a hook for adding environment  info in the html Report
def pytest_configure(config):

    if hasattr(config, 'metadata'):
     config.metadata['Project Name']="ATA"
     config.metadata['Module Name']="User Mangaement"
     config.metadata['Tester']="Salina"

#It is a hook for delete /Modify Environment info to HTML Report
    @pytest.hookimpl(optionalhook=True)
    def pytest_metadata(metadata):
        metadata.pop("JAVA_HOME", None)
        metadata.pop("Plugins", None)
