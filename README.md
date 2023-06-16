# Spotify-Album-Selector
A program that reads your saved albums on Spotify and chooses one at random for you to listen to

How to set up:

1. Install the spotipy library by running `pip install spotipy` for Mac or `py -m pip install spotipy` for Windows in your terminal. If that doesn't work, [read this](https://pypi.org/project/spotipy/) and figure it out.
2. Log in to [Spotify's developer website](https://developer.spotify.com/) and click on your profile in the top right corner of your screen
3. Select 'Create App' and set the app name and description to whatever you want.
4. Set the redirect uri to http://google.com/
5. Click 'Save'.
6. Click 'Settings'
7. Replace `['CLIENT_ID']` and `['CLIENT_SECRET']` in `album_selector.py` with your Client ID and Client Secret.
8. Run the program

- After you log into Spotify and authenticate the app, you will be redirected to Google's homepage. Copy the link and paste it into your terminal and press enter.

- When you do this, a `.cache` file will be created. This stores your access token, the token type, when it expires (valid for 1 hour), and the refresh token. For the next hour, you will be able to run the album selector as many times as you want. After the hour, you will have to re-authenticate the app for it to view your profile information.
