from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-public playlist-modify-private",
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt",
        username=os.getenv("SPOTIPY_USERNAME")
    )
)
user_id = sp.current_user()["id"]

date = input("What year would you like to travel to?[YYYY-MM-DD]: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

song_titles = soup.select("li ul li h3")
song_names = []
for song_title in song_titles:
    song_name = song_title.getText().strip()
    song_names.append(song_name)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


def create_playlist(playlist_Name):
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user_id, playlist_Name)
    return playlist['id']


def add_tracks_to_playlist(playlist_Id, song_uriss):
    sp.playlist_add_items(playlist_Id, song_uriss)


playlist_name = date + " Billboard hot 100"
playlist_id = create_playlist(playlist_name)
add_tracks_to_playlist(playlist_id, song_uris)
