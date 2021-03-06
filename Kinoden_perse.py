#%%
import requests
import bs4
# %%
res = requests.get('https://elib.maruzen.co.jp/elib/html/BookList?17')
print(res.text)
# %%
