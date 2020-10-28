import requests
import json

mathdroidAPI = "https://covid19.mathdro.id/api/countries/"
travelAdvisoryAPI = "https://www.travel-advisory.info/api?countrycode="
messagesAPI = "http://localhost:8000/api/messages/"


def get_data():
    url = mathdroidAPI
    r = requests.get(url)
    data = r.json()
    return data
