from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def test_firefox_session():
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.quit()

test_firefox_session()
