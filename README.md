# Spotify Playlist Creator

This Python script allows you to create a Spotify playlist based on Billboard Hot 100 songs from a specific date. It utilizes web scraping with BeautifulSoup to retrieve the song names from the Billboard website and the Spotipy library to interact with the Spotify API for playlist creation.

## Prerequisites

Before running the script, make sure you have the necessary dependencies installed:

```bash
pip install spotipy beautifulsoup4 python-dotenv
```

## Getting Started

1. **Spotify Developer Account:**
   - Create a Spotify Developer account and set up a new application to obtain the client ID and client secret. [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)

2. **Environment Variables:**
   - Create a `.env` file in the project directory with your Spotify application credentials:

   ```env
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   SPOTIPY_REDIRECT_URI=http://example.com
   SPOTIPY_USERNAME=YourSpotifyUsername
   ```

3. **Run the Script:**
   - Execute the script in your terminal:

   ```bash
   python your_script.py
   ```

   - Enter the desired year when prompted.

4. **Results:**
   - The script will create a Spotify playlist with the Billboard Hot 100 songs from the specified date.

## Important Note

- The script uses web scraping, and its functionality may be affected if the structure of the Billboard website changes.
- Ensure that you keep your Spotify credentials secure. Do not share them in your code or public repositories.

Feel free to customize the script for your needs and explore additional features provided by the Spotipy library.
