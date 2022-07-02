from playwright.sync_api import sync_playwright
import time
import config
USN = config.USN
PWD = config.PWD


def run(playwright):
    pagecontent = []
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    page.goto("https://kinoden.kinokuniya.co.jp/tohoku-univ/")
    page.click("//span[normalize-space(.)='学認でサインイン']")
    page.click("input[name=\"j_username\"]")
    page.fill("input[name=\"j_username\"]", "XXXXXXXX")
    page.click("input[name=\"j_password\"]")
    page.fill("input[name=\"j_password\"]", "XXXXXXXX")
    page.click("text=\"Login\"")
    with page.expect_navigation():
        page.click("input[name=\"_eventId_proceed\"]")
    page.click("text=\"検索\"")
    page.uncheck("input[type=\"checkbox\"]")
    page.click(
        "//div[normalize-space(.)='出版日順' and normalize-space(@role)='button']")
    time.sleep(2)
    r = 1
    for r in range(1, 22):
        time.sleep(2)
        print("newPage")
        content = page.content()
        pagecontent.append(content)
        print(f"{r}:append")
        if r == 21:
            break
        else:
            page.click(f"text=\"{r+1}\"")
            r += 1

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()
    return pagecontent


with sync_playwright() as playwright:
    pages = run(playwright)
    f = open('kinokuniya2.html', 'a')
    f.writelines(pages)
    f.close()

# %%
