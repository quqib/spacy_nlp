import spacy
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 UOS Community'
}

url = 'http://www.ccgp-jiangsu.gov.cn/pss/jsp/relevantCgggGetById.jsp'

params = {
    'ggid': '501b966e24d647faabccf1c25498c00b'
}

res = requests.post(url, params=params, headers=headers)

resJson = res.json()

content = BeautifulSoup(resJson.get('data').get('content'), 'lxml').text

nlp = spacy.load("zh_core_web_sm")

doc = nlp(content)

# print(doc)

for ent in doc.ents:
    print(ent.text, ent.label_)



