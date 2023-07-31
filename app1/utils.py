import requests
import json

def get_all_countries():
    url = "https://restcountries.com/v3.1/all"

    response = requests.get(url)

    countries_response_json = json.loads(response.text)

    countries_list = []

    for country in countries_response_json:
        countries_list.append(country['name']['common'])


    return sorted(countries_list)