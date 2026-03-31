import requests


def fetch_gecex_resolutions_from_camex():
    # Function to fetch GECEX resolutions from CAMEX
    url = 'https://www.gov.br/camex/pt-br/legislacao/resolucoes'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text  # or parse and return relevant data
    return None


def fetch_gecex_resolutions_from_portal_ex_tarifario():
    # Function to fetch GECEX resolutions from Portal Ex-Tarifário
    url = 'https://www.gov.br/portal-ex-tarifario'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text  # or parse and return relevant data
    return None


def fetch_gecex_resolutions_from_lexml():
    # Function to fetch GECEX resolutions from LexML API
    url = 'https://www.lexml.gov.br/lexml/api/resolutions'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # assuming we want JSON data
    return None
