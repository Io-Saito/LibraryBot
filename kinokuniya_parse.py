# %%
import re
from bs4 import BeautifulSoup
# %%
f = open('kinokuniya2.html', 'r')
# %%
soup = BeautifulSoup(f, 'html.parser', from_encoding="utf-8")

# %%
test = soup.find_all(
    "div", class_=re.compile(r"MuiPaper-root MuiCard-root jss([0-9]){3,4} MuiPaper-elevation1 MuiPaper-rounded"))
print(len(test))
# %%


def paren_cut(str):
    list = str.split("(")
    left = list[0]
    right = list[1].replace(")", "")
    return left, right

# %%


def get_data(X):
    # 書名[0]/出版社・出版年[2]/作者[1]/説明[3]
    span_list = list(map(lambda x: "jss"+str(x), list(range(436, 4384, 188))))
    a_list = list(map(lambda x: "jss"+str(x), list(range(446, 4394, 188))))
    list_ = X.find_all("span", class_=[span_list])
    test_list = list(map(lambda x: x.get_text(), list_))
    href__ = X.find_all("a", class_=[a_list])
    if len(href__) > 0:
        hrefs = X.find_all("a", class_=[a_list])[0]["href"]
    else:
        hrefs = None
    link = "https://kinoden.kinokuniya.co.jp" + hrefs if hrefs != None else None
    if len(test_list) == 5:
        title = test_list[0]+"【"+test_list[1]+"】"
        author = test_list[2]
        publish, publish_date = paren_cut(test_list[3])
    else:
        if "(" in test_list[2]:
            title = test_list[0]
            author = test_list[1]
            publish, publish_date = paren_cut(test_list[2])
        else:
            title = test_list[0]+"【"+test_list[1]+"】"
            author = test_list[2]
            publish, publish_date = paren_cut(test_list[3])

    data = {
        "title": title,
        "author": author,
        "publish": publish,
        "publish_date": publish_date,
        "link": link,
        "from": "Kinoden"
    }
    return data


# %%
data_list = []
for x in test:
    data_list.append(get_data(x))


# %%
