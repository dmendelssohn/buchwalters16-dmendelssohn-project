import requests

import json





def find_song_info(artist, title):

    url = 'http://developer.echonest.com/api/v4/song/search'

    params = {'api_key':'JTQT9YX9LIBIFRCDR', 'format':'json', 'results':1, 

    'artist': artist.lower(), 'title': title.lower(), 'bucket': 'audio_summary'}

    req = requests.get(url, params=params)

    if req.status_code != 200:

        return "Request not viable"

    else:

        data = req.json()

        if data['response']['songs']==[]:

            return "No songs match query"

        else:

            return data
