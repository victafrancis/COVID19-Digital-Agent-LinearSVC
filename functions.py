from spellchecker import SpellChecker
from bs4 import BeautifulSoup
import requests
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

def getInfoAllCountries(data):
    for country in data:
        if(getCountry(country)=='All'):
            print(country)
            return country

def getCountry(obj):
    return obj['country']

def getData():
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "621ab480a4mshd2ef8d54af57c28p1b60c1jsn0ab07455ea52"
    }

    response = requests.request("GET", url, headers=headers)
    # only get the data from the response
    data = response.json()['response']

    data = getInfoAllCountries(data)

    output ={}

    output['infected'] = data['cases']['total']
    output['recovered'] = data['cases']['recovered']
    output['deaths'] = data['deaths']['total']

    output['death_rate'] = str(round((output['deaths']/output['infected'])*100,2)) + '%'
    output['recovery_rate'] = str(round((output['recovered']/output['infected'])*100,2)) + '%'

    return output


# def getData():
#     url = 'https://www.worldometers.info/coronavirus/'
    
#     html_page = urlopen(url).read()
#     soup = BeautifulSoup(html_page, 'html.parser')

#     data = {}

#     data['infected'] = soup.find("div", {"class": "maincounter-number"}).find("span", text=True).text
#     data['recovered'] = soup.find_all("div", {"class": "maincounter-number"})[2].find("span", text=True).text
#     data['deaths'] = soup.find_all("div", {"class": "maincounter-number"})[1].find("span", text=True).text

#     deaths = int(removeSpecialCharacters(data['deaths']))
#     recovery = int(removeSpecialCharacters(data['recovered']))
#     infected = int(removeSpecialCharacters(data['infected']))

#     data['death_rate'] = str(round((deaths/infected)*100,2)) + '%'
#     data['recovery_rate'] = str(round((recovery/infected)*100,2)) + '%'

#     return data