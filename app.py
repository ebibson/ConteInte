import requests


r = requests.get("https://www.youtube.com")

def get_statuscode():
    return r.status_code

