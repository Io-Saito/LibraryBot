# %%
import re
from bs4 import BeautifulSoup
# %%
f = open('japan1.html', 'r')
# %%
soup = BeautifulSoup(f, 'html.parser', from_encoding="utf-8")

# %%
test = soup.find_all("div", class_="item")

# %%


def get_data(X, index):
    if X.find("p", class_="note") != None:
        return None
    title = X.find("div", class_="title").get_text()
    author = X.find("div", class_="author").get_text()
    li = X.find("a")["href"]
    if li != None:
        link = "https://japanknowledge.com"+li
    else:
        link = None
    if index < 800:
        pub_date = X.find("div", class_="pubDate").get_text().replace(
            "年", "/").replace("月刊", "")
        publish = "東洋文庫"
    elif 800 <= index <= 887:
        pub_date = None
        publish = "新日本古典文学"
    else:
        pub_date = X.find("div", class_="pubDate").get_text().replace(
            "年", "/").replace("月刊", "")
        publish = "文庫クセジュ"
    data = {
        "title": title,
        "author": author,
        "publish": publish,
        "publish_date": pub_date,
        "link": link,
        "from": "JapanKnowledge"
    }
    return data


# %%
data_list = []
for i, x in enumerate(test):
    n = get_data(x, i)
    if n is not None:
        data_list.append(n)


# %%
