"""
en res se carga todo lo que devuelve la pagina, todo el html.
Con select, vamos a la documentacion de bs4 y vemos que poner
para obtener que cosa segun sea clase, tag, etc.
Si veo en la pagina un titulo, le doy click derecho, inspeccionar, a ver que es
Por ejemplo, los links de los titulos, tienen el atributo "href"

para scrapping, podemos usar esta biblioteca beautifulsoup, pero hay algo ams complero, el
framework scrappy, https://scrapy.org/, pero es mas completo y hay que aprenderlo bien.
Si hago mucho scrapping, chequearlo.
De todas maneras, andes de hacer codigo, ver si la pagina que voy a revisar, no tiene una API que pueda usar.
"""

import requests
from bs4 import BeautifulSoup
from functools import reduce

cant = int(input("cuantas paginas quiere obtener?"))

res = []
for i in range(cant):
    res.append(requests.get(f"https://news.ycombinator.com/news?p={i+1}"))

soup = []
for i in range(cant):
    soup.append(BeautifulSoup(res[i].text, "html.parser"))

links = []
for i in range(cant):
    links.append(soup[i].select(".titlelink"))

subtexts = []
for i in range(cant):
    subtexts.append(soup[i].select(".subtext"))


def sumadorReduce(acc, item):
    return acc + item


allLinks = reduce(sumadorReduce, links)
allSubtexts = reduce(sumadorReduce, subtexts)


def customHn(allLinks, allSubtexts):
    hn = []
    for i, item in enumerate(allLinks):
        title = allLinks[i].getText()
        href = allLinks[i].get("href", None)
        vote = allSubtexts[i].select(".score")
        if len(vote):
            hn.append({"title": title, "link": href, "votes": int(
                vote[0].getText().replace(" points", ""))})
    return hn


def sortByVotes(list):
    return sorted(list, reverse=True, key=lambda item: item["votes"])


def showList(list):
    for i, item in enumerate(list):
        print(i+1, item["title"])
        #print(item["title"], item["link"], item["votes"], "", sep="\n")


data = customHn(allLinks, allSubtexts)
min = int(input("puntaje minimo: "))
data2 = list(filter(lambda item: item["votes"] >= min, data))
data2 = sortByVotes(data2)
showList(data2)
