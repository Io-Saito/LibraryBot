from playwright.sync_api import sync_playwright
import time
import config


def run(playwright):
    pagecontent = []
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://elib.maruzen.co.jp/elib/html/GuestLogin?1")
    page.click("text=\"学認アカウントをお持ちの方はこちら\"")
    page.click("img[id=\"dropdown_img\"]")
    page.click("text=\"東北大学\"")
    page.click("input[name=\"Select\"]")
    page.fill("input[name=\"j_username\"]", "XXXXXXXX")
    page.click("input[name=\"j_password\"]")
    page.fill("input[name=\"j_password\"]", "XXXXXXXX")
    page.click("text=\"Login\"")
    with page.expect_navigation():
        page.click("input[name=\"_eventId_proceed\"]")

    time.sleep(0.5)
    page.goto(
        "https://elib.maruzen.co.jp/elib/html/BookList/P3/true/SS/DESCREGIST_DESC?26")
    time.sleep(0.5)
    r = 0
    for r in range(0, 5):
        print("newPage")
        time.sleep(0.5)
        content = page.content()
        pagecontent.append(content)
        print("append")

        if r == 350:
            break
        else:
            page.click("text=\"次へ >\"")
            r += 1
    page.close()

    # ---------------------
    context.close()
    browser.close()
    return pagecontent


with sync_playwright() as playwright:
    pages = run(playwright)
    f = open('myfile_all_.html', 'a')
    f.writelines(pages)
    f.close()
