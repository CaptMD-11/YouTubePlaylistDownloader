from pytube import Playlist
from art import *


def get_urls_from_playlist(playlist_link):
    urls = []
    urls_from_playlist = Playlist(playlist_link)
    for url in urls_from_playlist:
        urls.append(url)


print(get_urls_from_playlist(
    'https://www.youtube.com/playlist?list=PL1EBE78CC528B52E8'))
