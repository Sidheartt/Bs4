from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# print(soup.prettify())

tags = soup.find_all(name="a")

for tag in tags:
    #print(tag.get("href"))
    #print(tag.getText())
    pass

head = soup.find(name="h1", id="name")
print(head.getText())

company_url = soup.select_one(selector="p a") #selector html selectors
print(company_url)

name = soup.select_one(selector="#name") # by select by # i.e id
print(name)

headd = soup.select_one(".heading") # selected by . i.e class
print(headd)