from behave import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


@given('I launch chrome browser')
def launch_chrome_browser(context):
    context.driver = webdriver.Chrome(executable_path="./chromedriver.exe")


@when('I open orange hrm homepage')
def open_url(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def enter_detail(context, user, pwd):
    try:
        ele_username = context.driver.find_element_by_id("txtUsername")
        ele_password = context.driver.find_element_by_id("txtPassword")
        ele_username.send_keys(user)
        ele_password.send_keys(pwd)
    except NoSuchElementException:
        context.driver.quit()


@when('I Click login button')
def click_login(context):
    try:
        ele_login = context.driver.find_element_by_id("btnLogin")
        ele_login.click()
    except NoSuchElementException:
        context.driver.quit()
        print("Unable to locate Login button")


@then('Successfully login to dashboard page')
def check_dashboard(context):
    try:
        dashboard = context.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/h1").text
    except NoSuchElementException:
        context.driver.quit()
        assert(False, "Test Failed")
        print("Unable to Locate dashboard")
    if dashboard == "Dashboard":
        assert(True, "Test Passed")