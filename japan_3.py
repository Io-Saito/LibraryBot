from playwright.sync_api import sync_playwright
import time


def run(playwright):
    pagecontent = []
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    page.goto("https://japanknowledge.com/library/")
    page.click("text=\"ログインする\"")
    page.click("text=\"学術認証（シボレス）でのご利用はこちら\"")
    page.click("img[id=\"dropdown_img\"]")
    page.click("text=\"東北大学\"")
    page.click("input[name=\"Login\"]")
    page.click("input[name=\"j_username\"]")
    page.fill("input[name=\"j_username\"]", "XXXXXXXX")
    page.click("input[name=\"j_password\"]")
    page.fill("input[name=\"j_password\"]", "XXXXXXXX")
    page.click("text=\"Login\"")
    with page.expect_navigation():
        page.click("input[name=\"_eventId_proceed\"]")
    pagecontent = []
    page.click("text=\"本棚\"")
    page.click("img[alt=\"東洋文庫\"]")
    r = 1
    for r in range(1, 68):
        time.sleep(2)
        print("newPage")
        content = page.content()
        print(content)
        pagecontent.append(content)
        print(f"東洋文庫{r}:append")
        if r == 67:
            break
        else:
            page.click("text=\"次>\"")
            r += 1
    page.click("text=\"本棚\"")
    page.click("img[alt=\"新編 日本古典文学全集\"]")
    n = 1
    for n in range(1, 10):
        time.sleep(2)
        print("newPage")
        content = page.content()
        print(content)
        pagecontent.append(content)
        print(f"古典文学{n}:append")
        if n == 9:
            break
        else:
            page.click("text=\"次>\"")
            n += 1

    page.click("text=\"本棚\"")
    page.click("img[alt=\"文庫クセジュ ベストセレクション\"]")
    k = 1
    for k in range(1, 37):
        time.sleep(2)
        print("newPage")
        content = page.content()
        print(content)
        pagecontent.append(content)
        print(f"クセジュ{k}:append")
        if k == 36:
            break
        else:
            page.click("text=\"次>\"")
            k += 1
    # assert page.url == "https://japanknowledge.com/lib/shelf/quesaisje/"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()
    return pagecontent


with sync_playwright() as playwright:
    pages = run(playwright)
    f = open('japan1.html', 'a')
    f.writelines(pages)
    f.close()
