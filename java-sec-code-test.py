import time
import argparse
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

from webdriver_manager.firefox import GeckoDriverManager

# taken straight from the selenium docs, use this for general
# network verification
def test_google():
    options = FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.google.com")
    driver.title # => "Google"

    driver.implicitly_wait(2.0)

    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")

    search_box.send_keys("Selenium")
    search_button.click()

    search_box = driver.find_element(by=By.NAME, value="q")
    assert search_box.get_attribute("value") == "Selenium"
    
    driver.quit()

# Initialize the browser driver
def driver_init(host, port, options):
    driver = webdriver.Firefox(options=options)
    driver.get("http://" + host + ":" + port)
    driver.title # => "JavSecCode"
    return(driver)

# Handle the highly secure java-sec-code login page
def java_sec_code_login(driver):
    driver.implicitly_wait(2.0)
    user_box = driver.find_element(by=By.NAME, value="username")
    pw_box = driver.find_element(by=By.NAME, value="password")
    login_button = driver.find_element(by=By.XPATH, value='/html/body/div/div/button')

    user_box.send_keys("admin")
    pw_box.send_keys("admin123")
    login_button.click()

# find the element
# click the element
# sleep a bit just for show (can probably take it out)
# hit the back button
def clicky_clicky(driver, link):
    appinfo = driver.find_element(by=By.LINK_TEXT, value=link)
    appinfo.click()
    time.sleep(1)
    driver.execute_script("window.history.go(-1)")

# Follow all the links on the index page
# TODO some of these open screens with additional buttons to click
def java_sec_code_links(driver):
    # not sure if we need to wait, but assuming so for now
    driver.implicitly_wait(2.0)
    # the typo below is not mine!!
    clicky_clicky(driver, "Application Infomation")
    clicky_clicky(driver, "Swagger")
    clicky_clicky(driver, "CmdInject")
    clicky_clicky(driver, "JSONP")
    clicky_clicky(driver, "Picture Upload")
    clicky_clicky(driver, "File Upload")
    clicky_clicky(driver, "Cors")
    clicky_clicky(driver, "PathTraversal")
    clicky_clicky(driver, "SqlInject")
    clicky_clicky(driver, "SSRF")
    clicky_clicky(driver, "RCE")
    clicky_clicky(driver, "ooxml XXE")
    clicky_clicky(driver, "xlsx-streamer XXE")
    clicky_clicky(driver, "logout")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Java-Sec-Code Button Clicker')
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default='8080')
    parser.add_argument('--headless', action='store_true')
    args = parser.parse_args()

    options = FirefoxOptions()
    if (args.headless):
        options.add_argument("--headless")

    #test_google()
    driver = driver_init(args.host, args.port, options)
    java_sec_code_login(driver)
    java_sec_code_links(driver)
    driver.quit()
