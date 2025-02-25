import time

from playwright.sync_api import Page, expect


def test_playwrigthbasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() #do some opreations
    page = context.new_page()
    page.goto("https://google.com")


def test_playwrightshortcut(page:Page):
    page.goto("https://google.com")


def test_login(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning123")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()



