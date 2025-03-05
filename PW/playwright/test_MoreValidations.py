import time
from playwright.sync_api import Page, expect


def test_UIChecks(page: Page):

    #hide / display  and placeholder

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


    # AlertBoxes
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()
    time.sleep(4)

    #mouse hower
    page.locator("//button[@id='mousehover']").hover()
    page.get_by_role("link",name="Top").click()


    #frame handling
    #pageFrame = page.frame_locator("#courses-iframe")
    pageFrame = page.frame_locator("//iframe[@id='courses-iframe']")
    pageFrame.get_by_role("link",name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")


    #handle data table
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")


    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="Price").count()>0:
            priceColVal = i
            print("Price column value is ",priceColVal)
            break

    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(priceColVal)).to_have_text("37")


# To generate the code using record and playback feature please use
#  playwright codegen url
# eg: playwright codegen https://rahulshettyacademy.com/client









