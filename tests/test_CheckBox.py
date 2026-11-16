import re
import time
from playwright.sync_api import Page,expect,Playwright,sync_playwright

def test_checkbox(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=True) #para que abra el navegador y la velocidad de procesamiento 
    context=browser.new_context(#para que haga lo que esta dentro 
        viewport={'width':1500, 'height':800}
    )
    page=context.new_page()
    page.goto("https://demoqa.com/checkbox")
    page.add_style_tag(content="""adplus-anchor, #fixedban, footer, iframe { display: none !important; } """)
    expect(page).to_have_title("demosite")
    che1=page.locator(".rc-tree-switcher")#HOME
    expect(che1).to_be_visible()
    che1.click()
    page.locator("xpath=//span[@title='Documents']/preceding-sibling::span[contains(@class, 'rc-tree-switcher')]").click()
    page.locator("xpath=//span[@title='Office']/preceding-sibling::span[contains(@class, 'rc-tree-switcher')]").click()
    page.locator("//span[contains(@aria-label,'Select Private')]").click()
    browser.close()
