import requests
import pandas as pd
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
        if data['response']['songs'] == []:
            return "No songs match query"
        if data['response']['status']['message'] != 'Success':
            return "There was a problem finding the song"
        else:
            return data


def create_df(songs):
    song_list = []
    for song in songs:
        info = find_song_info(song[0], song[1])
        song_dict = info['response']['songs'][0]['audio_summary']
        song_dict['artist_name'] = info['response']['songs'][0]['artist_name']
        song_dict['artist_id'] = info['response']['songs'][0]['artist_id']
        song_dict['title'] = info['response']['songs'][0]['title']
        song_dict['id'] = info['response']['songs'][0]['id']
        song_list.append(song_dict)
    df = pd.DataFrame(song_list)
    df = df.drop(['audio_md5','key','time_signature','mode','analysis_url','acousticness','valence','instrumentalness','speechiness'],axis=1)
    df = df.sort('danceability').reset_index()
    df = df.drop('index',axis=1)
    return df
