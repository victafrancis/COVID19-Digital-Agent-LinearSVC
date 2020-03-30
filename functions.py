from spellchecker import SpellChecker
from bs4 import BeautifulSoup
import requests
import time
from dateutil import parser
from datetime import datetime, timezone

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
    allData = response.json()['response']

    data = getInfoAllCountries(allData)

    output ={}

    output['infected'] = data['cases']['total']
    output['recovered'] = data['cases']['recovered']
    output['deaths'] = data['deaths']['total']

    output['death_rate'] = str(round((output['deaths']/output['infected'])*100,2)) + '%'
    output['recovery_rate'] = str(round((output['recovered']/output['infected'])*100,2)) + '%'

    output['datetime'] = getDatetime(data)

    return output

def getDatetime(data):
    date = data['time']
    datetime_object = parser.parse(date)
    datetime_object = utc_to_local(datetime_object)
    return datetime_object.strftime("%d %b %Y, %H:%M:%S")

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)