#realiza busca no site jusbrasil

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from requests import get

keyslist = ["APTE", "APELANTE", "AUTOR"]

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',}

file = open('novo.txt', 'r')
nfile = open('result.txt', 'w')

for row in file:

    url = "https://www.jusbrasil.com.br/busca?q="
    url += row
    req = Request(url, headers=headers)
    page = urlopen(req).read()

    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    aux = html_soup.find_all('div', class_ = 'EntitySnippet-anchor-wrapper')
    print(len(aux))
    #abre primeiro link
    search = ''
    try:
        search = aux[0].a.attrs['href']
    except:
        search = False

    result = ''
    if search != False:
        search = search[:-9]
        print(search)
        #busca
        req = Request(search, headers=headers)
        page2 = urlopen(req).read()
        response = get(search)
        html_search = BeautifulSoup(response.text, 'html.parser')
        doc = html_search.find_all('div', class_ = 'LawsuitJournalBlock-body')
        x = len(doc)
        print(x)
        result = ''
        for i in range(x):
            part = doc[i].findAll('p')
            for p in part:
                words = p.text
                words = words.replace(':',' ')
                words = words.split()
                if words[0] in keyslist:
                    print(p.text)
                    result = " ".join(words[1:])
            if result != '': break

        print(result)
    else:
        result = '?'

    aux = row + " " + result + "\n"
    nfile.write(aux)
   

file.close()
nfile.close()

    




