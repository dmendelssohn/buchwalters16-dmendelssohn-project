import DDR
import requests
import json
import numpy

def song_calc(song_lst):
    if len(song_lst) > 10:
        return numpy.mean(song_lst),numpy.sd(song_lst)
    return "This playlist is not long enough to use these measurements"    

class Song():
    
    def __init__(self,title,artist):
        data_dict = DDR.find_song_info(artist,title)['response']['songs'][0]
        self.title = data_dict['title']
        self.artist = data_dict['artist_name']
        self.artist_id = data_dict['artist_id']
        self.length = data_dict['audio_summary']['duration']
        self.danceability = data_dict['audio_summary']['danceability']
        self.tempo = data_dict['audio_summary']['tempo']
        self.energy = data_dict['audio_summary']['energy']
        self.song_id = data_dict['id']


    def __repr__(self):
        return "{} performed by {}".format(self.title,self.artist)

class Playlist():
    
    def __init__(self,name):
        self.name = name
        self.songs_lst = []
        self.song_ids = []
        self.tempo =  song_calc([x.tempo for i in songs_lst])
        self.danceability = song_calc([x.danceability for i in songs_lst])
        self.energy = song_calc([x.energy for i in songs_lst])
        self.banned = []

    def __repr__(self):
        return str(self.name)

    def Songs(self):
        return [x.title for i in songs_lst]    

    def Add_to_Banned(self,title,artist):
        var = Song(title,artist)
        self.banned.append(Song(title,artist))
        return "{} by {} added to banned songs.".format(var.title,var.artist)

    def Add_Song(self,title,artist):
        var = Song(title,artist)
        if var.song_id in [x.song_id for x in self.songs_lst]
            return "{} by {} is banned at this party, asshole.".format(var.title,var.artist) 
        else:
            self.songs_lst.append(var)
            return "{} by {} has been added to the playlist.".format(var.title,var.artist)       
