import requests
from bs4 import BeautifulSoup


url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
r_html = r.text

# some requests code here for getting r_html 

soup = BeautifulSoup(r_html, "html.parser")
#print(soup)


title = soup.find('article')
title = title.h1.string

#print(title)
hed_text = soup.find('article').span.string
#print(hed_text)


art_text = soup.find_all('section', class_="content-section")
#art_text = art_text.find_all("p")
with open("ex19_rslt.txt", "w", encoding="utf-8") as fh:
    fh.write(title)
    fh.write("\n")
    fh.write(hed_text)
    fh.write("\n")
    for txt in art_text:
        txt2 = txt.find_all('p')
        for txt3 in txt2:
            fh.write(txt3.get_text())
            fh.write("\n\n")
        

