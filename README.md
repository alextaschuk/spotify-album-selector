# Spotify-Album-Selector
A locally-ran program that reads your saved albums from your Spotify account and chooses one at random for you to listen to.

**How to set up:**
- _Python3 is a pre-req for any of this to work._
1. Install the spotipy library by running `pip install spotipy` for Mac or `py -m pip install spotipy` for Windows in your terminal. If you're having trouble, [read this](https://pypi.org/project/spotipy/).
2. Log in to [Spotify's developer website](https://developer.spotify.com/) and click on your profile picture in the top right corner of your screen
3. Select 'Dashboard'.
4. Select 'Create App' and set the app name and description to whatever you want (e.g., "Random Album Selector").
5. Set the redirect uri to http://google.com/
6. Click 'Save'.
7. Click 'Settings'
8. Copy your client id and client secret and replace `['CLIENT_ID']` and `['CLIENT_SECRET']` in `album_selector.py`.

**How to use the program:**
- Run the program. When it is ran for the first time, a new window will open and ask for you to authorize for the program to see some of your user data. Click "Agree". 
- You will be redirected to a Google homepage. Copy the link and paste it into your terminal and press enter. 
- Wait a couple of seconds, and an album will be chosen and printed into the terminal. 

**Notes:**
- When you run the program, a `.cache` file will be created. This stores your access token, the token type, when it expires, and the refresh token.
- If you want to remove access to the program, visit [your account settings](https://www.spotify.com/us/account/apps/) and find the app that mactches the name of the app you created on Spotify's developer website (For example, if my app is called "Album Selector", there would be an app on my account settings page also called "Album Selector"). Click "Remove Access".
