# pip install pytest
# playwright install - this is optional step

# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()

# with pytest we do not need the above steps, it automatically delclares the browsers, context, page

#pytest  by defatult starts the above process
# the def should start with test_
#the file name should start with test_ or should end with _test

# to trigger this, we need to pass the command on terminal as pytest filename 
# for example here the command will be pytest test_examplePytest.py

# it will run in headless mode and if we want to see the execution we need to pass --headed
# or we cna pass the browser also  pytest test_examplePytest.py --headed --browser chromium
# we can use -s to print the print statements
# for getting the status of testcase we can use -vv

# pytest will not have the dependendy from one test case to another; hence if one fails, it will not happen the other function exeuction



def test_login_test1(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("inside test1")

#by default, it will create separate context for each test case
def test_login_test2(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("inside test2")

# we need not call the functions to execute it
#if we test as prefex or suffix, it will be executed directly
