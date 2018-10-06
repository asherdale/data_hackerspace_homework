import requests
import re
import matplotlib.pyplot as plt
import numpy as np


def lyrics_word_count_easy(artist, song, phrase):
    lyrics_response = requests.get('https://api.lyrics.ovh/v1/' + artist + '/' + song)

    lyrics_key = 'lyrics'

    if lyrics_key not in lyrics_response.json():
        return -1
    
    return lyrics_response.json()[lyrics_key].lower().count(phrase.lower())

def lyrics_word_count(artist, phrase):
    musix_match_key = 'c187a80da5c41314c41c894c79081f8a'

    artist_info = requests.get('http://api.musixmatch.com/ws/1.1/artist.search?apikey=' + musix_match_key + '&q_artist=' + artist + '&page_size=1')
    artist_list = artist_info.json()['message']['body']['artist_list']

    if len(artist_list) == 0:
        return -1

    artist_id = artist_list[0]['artist']['artist_id']

    albums_info = requests.get('http://api.musixmatch.com/ws/1.1/artist.albums.get?page_size=100&apikey=' + musix_match_key + '&artist_id=' + str(artist_id))
    album_list = albums_info.json()['message']['body']['album_list']

    artist_tracks = []

    phrase_count = 0

    for album in album_list:
        album_id = album['album']['album_id']
        album_tracks = requests.get('http://api.musixmatch.com/ws/1.1/album.tracks.get?page_size=74&apikey=' + musix_match_key + '&album_id=' + str(album_id))
        
        track_list = album_tracks.json()['message']['body']['track_list']

        for track in track_list:
            artist_tracks.append(track['track']['track_name'].lower())
    
    unique_tracks = set(artist_tracks)

    for track in unique_tracks:
        num_phrases = lyrics_word_count_easy(artist, track, phrase)
        phrase_count += num_phrases if num_phrases > -1 else 0

    return phrase_count

def visualize():
    x = np.array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9.,10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25., 26., 27., 28., 29.])
    y= np.array([ 0., 25., 27., 4., -22., -28., -8., 19., 29., 12., -16., -29., -16., 12., 29., 19., -8., -28.,-22., 4., 27., 25., -0., -25., -27., -3., 22., 28., 8., -19.])

    grid = plt.GridSpec(2, 2, wspace=0.3, hspace=0.3)

    plt.subplot(grid[0, 0:])
    plt.plot(x, y)
    plt.title("LineGraph")

    plt.subplot(grid[1, :1])
    plt.hist((x, y), histtype='bar')
    plt.title("Histogram")

    plt.subplot(grid[1, 1:])
    plt.scatter(x, y)
    plt.title("Scatter")

    return plt.show()

print(lyrics_word_count("martin garrix", "burn"))