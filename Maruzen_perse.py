# %%
from bs4 import BeautifulSoup
f = open('myfile_all_.html', 'r')
# %%
soup = BeautifulSoup(f, 'html.parser', from_encoding="utf-8")
# %%

Bookname = soup.find_all("div", class_="bookinfo")

# %%


def getinfo(x):
    # strong,span,ddタグの中身を文字列にした
    strong = list(map(lambda y: y.get_text(), x.find_all("strong")))
    span = list(map(lambda y: y.get_text(), x.find_all("span")))
    dd = list(map(lambda y: y.get_text(), x.find_all("dd")))
    # 閲覧用リンクを持ってくる
    link_ = x.find("a", class_="btl")
    if link_ is not None:
        link = "https://elib.maruzen.co.jp/elib/html/" + \
            "/".join(link_["href"].split("/")[4:7])
    else:
        link = None
    publish = dd[1] if len(dd) >= 2 else None
    publish_date = dd[2] if len(dd) >= 3 else None
    data = {
        "title": strong[0]+span[0],
        "author": dd[0],
        "publish": publish,
        "publish_date": publish_date,
        "link": link,
        "from": "Maruzen"
    }
    return data


# %%
li = []
for x in Bookname:
    y = getinfo(x)
    li.append(y)

# %%

# %%
