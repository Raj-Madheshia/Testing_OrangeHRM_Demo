import parse
from behave import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Important step to parse null data from features file else it will through error
@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


register_type(NullableString=parse_nullable_string)


@given('Launch ChromeBrowser')
def launch_chrome_browser(context):
    context.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Entered username is "{user:NullableString}" and password is "{pwd:NullableString}')
def login_check(context, user, pwd):
    try:
        ele_username = context.driver.find_element_by_id("txtUsername")
        ele_password = context.driver.find_element_by_id("txtPassword")
        if user:
            ele_username.send_keys(user)
        if pwd:
            ele_password.send_keys(pwd)
    except NoSuchElementException:
        context.driver.quit()


@then('Check Invalid message on screen')
def click_login_button(context):
    try:
        ele_login = context.driver.find_element_by_id("btnLogin")
        ele_login.click()
    except NoSuchElementException:
        context.driver.quit()
        print("Unable to locate Login button")

    try:
        invalid = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/span")))
        assert invalid.is_displayed, "Test Passed"
        if invalid.text == "Invalid credentials":
            assert True, "Test Passed for invalid login"
        elif invalid.is_displayed == "Username cannot be empty":
            assert True, "Test Passed for empty Username"
        elif invalid.is_displayed == "Password cannot be empty":
            assert True, "Test Passed for empty Password"
    except NoSuchElementException:
        context.driver.quit()
        print("Failed to find invalid element")
        assert False, "Test Failed"


@then('Close Browser')
def step_impl(context):
    context.driver.quit()


