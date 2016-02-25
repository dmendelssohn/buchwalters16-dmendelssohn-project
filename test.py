import DDR
import requests
import json
import numpy
from songobj import Song as Song
import pandas as pd


def playlist():
    value = input('Is this a new playlist?(Y/N)\n')
    if value.lower() not in ['y','n']:
        print("Please answer Yes(Y) or No(N)\n")
        playlist()
    elif value.lower() == 'y':
        flname = input("What would you like to call your playlist?\n") + ".txt"
        adding_songs(flname)

        print("Your playlist is saved as {}".format(flname))        
    else:
        filename = input("What is the name of your playlist?\n") +".txt"
    print('lit')



def adding_songs(filename):
    adding_songs = True
    while adding_songs:
        artist = input("What is the artist's name?\n")
        song = input("What is the song?\n")
        genre = input("What is the genre?\n")
        new_song = Song(song,artist)
        print(new_song)
        more_songs = input("Would you like to add another song?(Y/N)\n")
        if more_songs.lower() not in ['y','n']:
            more_songs = input("Please answer Yes(Y) or No(N)\n")
        if more_songs.lower() == 'n':
            adding_songs = False



if __name__ == "__main__":
    playlist()
    