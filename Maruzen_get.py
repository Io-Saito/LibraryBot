from playwright.sync_api import sync_playwright
import time


def run(playwright):
    pagecontent = []
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://elib.maruzen.co.jp/elib/html/GuestLogin?1
    page.goto("https://elib.maruzen.co.jp/elib/html/GuestLogin?1")

    # Click text="学認アカウントをお持ちの方はこちら"
    page.click("text=\"学認アカウントをお持ちの方はこちら\"")
    # assert page.url == "https://ds.gakunin.nii.ac.jp/WAYF?entityID=https%3A%2F%2Felib.maruzen.co.jp%2Fshibboleth-sp&return=https%3A%2F%2Felib.maruzen.co.jp%2FShibboleth.sso%2FDS%3FSAMLDS%3D1%26target%3Dss%253Amem%253Aec3407731dd41f5779dc4bf9f00b17307e8e48a7a7d201b4db3fb5091caecea4"

    # Click img[id="dropdown_img"]
    page.click("img[id=\"dropdown_img\"]")

    # Click text="東北大学"
    page.click("text=\"東北大学\"")

    # Click input[name="Select"]
    page.click("input[name=\"Select\"]")
    # assert page.url == "https://idp.auth.tohoku.ac.jp/idp/profile/SAML2/Redirect/SSO?execution=e1s1"

    # Click input[name="j_username"]
    page.click("input[name=\"j_username\"]")

    # Fill input[name="j_username"]
    page.fill("input[name=\"j_username\"]", "ju12028454")

    # Click input[name="j_password"]
    page.click("input[name=\"j_password\"]")

    # Fill input[name="j_password"]
    page.fill("input[name=\"j_password\"]", "KAlSi3O8")

    # Click text="Login"
    page.click("text=\"Login\"")
    # assert page.url == "https://idp.auth.tohoku.ac.jp/idp/profile/SAML2/Redirect/SSO?execution=e1s2"

    # Click input[name="_eventId_proceed"]
    # with page.expect_navigation(url="https://elib.maruzen.co.jp/elib/html/Top?3"):

    with page.expect_navigation():
        page.click("input[name=\"_eventId_proceed\"]")

    time.sleep(0.5)
    page.goto(
        "https://elib.maruzen.co.jp/elib/html/BookList/P3/true/SS/DESCREGIST_DESC?26")
    time.sleep(0.5)
    # B=page.content()
    # pagecontent.append(B)
    r = 0
    for r in range(0, 349):
        print("newPage")
        time.sleep(0.5)
        content = page.content()
        pagecontent.append(content)
        print("append")
        page.click("text=\"次へ >\"")
        r += 1
    page.close()

    # ---------------------
    context.close()
    browser.close()
    return pagecontent


with sync_playwright() as playwright:
    pages = run(playwright)
    f = open('myfile.html', 'a')
    f.writelines(pages)
    f.close()
