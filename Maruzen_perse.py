#%%
from bs4 import BeautifulSoup
f = open('myfile.html', 'r')
soup = BeautifulSoup(f, 'html.parser')
#%%
H2=soup.find_all("h2")
display(H2)
# %%
