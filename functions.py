from spellchecker import SpellChecker
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

# spell checker
spellcheck = SpellChecker()

def check(question):
    question = removeSpecialCharacters(question)
    words = question.split()
    # mispelled = spellcheck.unknown(words)
    output = []

    for word in words:
        if word != spellcheck.correction(word):
            output.append(spellcheck.correction(word))
        else:
            output.append(word)

    return ' '.join(output)


def removeSpecialCharacters(sentence):
    unwanted = "!@#$%^&*()[]}{;:,./<>?\|`~-=_+"

    for char in unwanted:
        sentence = sentence.replace(char, "")
    
    return sentence


def getData():
    url = 'https://www.worldometers.info/coronavirus/'
    
    html_page = urlopen(url).read()
    soup = BeautifulSoup(html_page, 'html.parser')

    data = {}

    data['infected'] = soup.find("div", {"class": "maincounter-number"}).find("span", text=True).text
    data['recovered'] = soup.find_all("div", {"class": "maincounter-number"})[2].find("span", text=True).text
    data['deaths'] = soup.find_all("div", {"class": "maincounter-number"})[1].find("span", text=True).text

    deaths = int(removeSpecialCharacters(data['deaths']))
    recovery = int(removeSpecialCharacters(data['recovered']))
    infected = int(removeSpecialCharacters(data['infected']))

    data['death_rate'] = str(round((deaths/infected)*100,2)) + '%'
    data['recovery_rate'] = str(round((recovery/infected)*100,2)) + '%'

    return data