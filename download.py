import requests
import zipfile
import html
import io

api = 'https://beatsaver.com/api/songs/new/{}'
dl = 'https://beatsaver.com/download/{}'

def get_total():
    resp = requests.get(api.format(0)).json()
    return resp['total']

def fetch_single(start: int):
    resp = requests.get(api.format(start)).json()
    return resp['songs']

def download(song):
    key = song['key']
    name = song['name']

    # If we know we've downloaded a song already, skip it
    if check_json(key):
        return

    # *unzips*
    zip_file = requests.get(dl.format(key)).content
    try:
        with zipfile.ZipFile(io.BytesIO(zip_file)) as song_zip:
            song_zip.extractall('CustomSongs/{}'.format(song['key']))
            
        # Save the fact we've downloaded this song
        write_json(key)
        print('Downloading {}'.format(name))
    except:
        print('Failed to download {}. An Error occoured'.format(html.unescape(name)))
