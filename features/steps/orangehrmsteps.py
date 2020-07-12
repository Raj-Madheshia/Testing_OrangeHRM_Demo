from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path="./chromedriver.exe")


@when('open orange hrm homepage')
def open_home_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that the logo present on page')
def verify_logo(context):
    status = context.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
    assert status is True


@then('close web browser')
def close_browser(context):
    context.driver.close()
