# Spotify playlist using the spotify api
import datetime as dt
import json
from bs4 import BeautifulSoup
import requests

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipy.util as util


travel_date = input("Which year do you want to travel to? Type the date in this format DD-MM-YYYY: ")
# travel_date = '22-12-1996'
travel_date = '-'.join([i for i in travel_date.split("-")[::-1]])
d = dt.date.fromisoformat(travel_date)
str_date = d.strftime('%Y-%m-%d')
billboard_scraping_url = 'https://www.billboard.com/charts/hot-100/'+str_date
res = requests.get(billboard_scraping_url)
soup = BeautifulSoup(res.text, 'lxml')
songs = soup.find_all('h3', class_='a-no-trucate')
singers = soup.find_all('span', class_='a-no-trucate')

spotify = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            username='username',
            scope='playlist-modify-public', client_id="client-id",
        client_secret="client-secret", redirect_uri='http://127.0.0.1:9090'))

user_id = "user-id"
playlist_name = str_date+" Billboard TOP 100"
playlist_id = spotify.user_playlist_create(spotify.me()['id'], playlist_name)


track_list = []

for i in range(len(songs)):
    # track = spotify.search(q=f'track: bent year: 2000 artist: matchbox twenty', limit=1, type='track')
    track = spotify.search(q=f'track: {songs[i].getText().strip()} year: {str_date[:4]} artist: {singers[i].getText().strip()}', limit=1, type='track')
    if len(track["tracks"]["items"]) < 1:
        continue
    print(f"Adding '{songs[i].getText().strip()}' by '{singers[i].getText().strip()}' to `{playlist_name}` playlist.")
    
    track_list.append(track["tracks"]["items"][0]["uri"])
    # track_id = "spotify:track:6fA7akEuTUL3dW1V0GELaZ"


spotify.playlist_add_items(playlist_id=playlist_id["uri"], items=track_list)
print(f"Finished adding {len(track_list)} tracks to playlist {playlist_name}")

# # with open("Day46_scraped.html") as file:# print(soup.prettify())

# #     soup = BeautifulSoup(file.read(), 'lxml')
   
# # items = soup.find_all(_class='o-chart-results-list__item')
# # print(items)
# # 12-08-2000


# print(len(songs))
# print(len(singers))
# for i in range(len(songs)):
#     print(songs[i].getText().strip()+" - "+singers[i].getText().strip())
 
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="[client id]", client_secret="client secret"))

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])


# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# util.prompt_for_user_token(username,scope,client_id='your-spotify-client-id',client_secret='your-spotify-client-secret',redirect_uri='your-app-redirect-url')

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# with open('Day46_spotify_json.json', "w") as f:
#     json.dump(track, f)
# spotify.play
# spotify.playlist_add_items(position=)
# print(playlist_id)

# for album in albums:
#     print(album['name'])
# spotify.user