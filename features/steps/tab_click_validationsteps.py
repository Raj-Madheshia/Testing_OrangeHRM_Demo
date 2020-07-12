from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


@when('Check Successful login in dashboad')
def step_impl(context):
    try:
        context.driver.find_element_by_id("welcome")
        assert True, "Test passed"
    except NoSuchElementException:
        assert False, "Homepage Not found"
        context.driver.quit()
    except():
        assert False, "Something went wrong"
        context.driver.quit()


@then('click on "{tab}"')
def step_impl(context, tab):
    try:
        tb = context.driver.find_element_by_id(tab)
        tb.click()
    except NoSuchElementException:
        assert False, "tab not found"
        context.driver.quit()
    except():
        assert False, "Something went wrong"
        context.driver.quit()


@then('check title name is "{heading}"')
def step_impl(context, heading):
    try:
        heading_data = context.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/h1").text
        if heading_data == heading:
            assert True, "Test Passed"
        else:
            assert False, "Test Failed"
    except NoSuchElementException:
        assert False, "Unable to locate heading"
        context.driver.quit()
    except():
        assert False, "Test Failed"
        context.driver.quit()


