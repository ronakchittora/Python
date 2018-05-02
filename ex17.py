import requests
from bs4 import BeautifulSoup


url = "http://www.nytimes.com/"
r = requests.get(url)
r_html = r.text
#print(r_html)

# some requests code here for getting r_html 

soup = BeautifulSoup(r_html, "html.parser")
#print(soup)


#title = soup.find_all("article")
title = soup.find_all('h2', class_="story-heading")
with open("ex17_rslt2.txt", "w", encoding="utf-8") as fh:
    for txt in title:
        if txt.find("a"):
            txt2 = txt.a
            #print(txt1.get_text())
            fh.write(txt2.get_text().strip())
            fh.write("\n")
        else:
            txt2 = txt.contents[0]
            fh.write(txt2 + "\n")

'''
with open("ex17_rslt.txt", "w", encoding="utf-8") as fh:
    for txt in title:
        if txt.find("h2"):
            txt1 = txt.h2
            if txt1.find("a"):
                txt2 = txt1.a
                #print(txt1.get_text())
                fh.write(txt2.get_text())
                fh.write("\n")

'''


"""
url = 'http://www.nytimes.com/'
ttl_lst = []

soup = BeautifulSoup(requests.get(url).text)
title = soup.findAll('h2', {'class': 'story-heading'})
for row in title:
     ttl_lst.append(row.text)

print(ttl_lst)
"""
"""
# the URL of the NY Times website we want to parse
base_url = 'http://www.nytimes.com'

# the syntax (according to the documentation) for how to 
# "load" a webpage through Python
r = requests.get(base_url)

# how to decode the text of the HTML of the NY Times homepage
# website. r comes from the requests request above
soup = BeautifulSoup(r.text)

# find and loop through all elements on the page with the 
# class name "story-heading"
for story_heading in soup.find_all(class_="story-heading"): 
    # for the story headings that are links, print out the text
    # and format it nicely
    # for the others, take the contents out and format it nicely
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
"""
