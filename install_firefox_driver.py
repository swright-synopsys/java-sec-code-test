from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

def test_firefox_session():
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(service=service, options=options)
    driver.quit()

test_firefox_session()
