import requests

api = 'https://beatsaver.com/api/songs/new/{}'
dl = 'https://beatsaver.com/download/{}'

def get_total():
    resp = requests.get(api.format(0)).json()
    return resp['total']

def fetch_single(start: int):
    resp = requests.get(api.format(start)).json()
    return resp['songs']
