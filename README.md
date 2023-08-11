# Spotify-Album-Selector
A locally-ran program that reads your saved albums from your Spotify account and chooses one at random for you to listen to.

**How to set up:**
- _Python3 is a pre-req for this to work._
1. Download the `album_selector.py` file from this repository.
2. Install the spotipy library by running `pip install spotipy` for Mac or `py -m pip install spotipy` for Windows in your terminal. If you're having trouble, [read this](https://pypi.org/project/spotipy/).
3. Log in to [Spotify's developer website](https://developer.spotify.com/) and click on your profile picture in the top right corner of your screen
4. Select 'Dashboard'.
5. Select 'Create App' and set the app name and description to whatever you'd like (e.g., "Album Selector").
6. Set the redirect uri to http://google.com/
7. Click 'Save'.
8. Click 'Settings'
9. Copy your Client ID and open `album_selector.py` in a text editor (like VS Code).
10. Replace `['CLIENT_ID']` on line 5 with the copied value in the python file.
11. Copy your Client secret (can be viewed by selecting 'View client secret') and replace `['CLIENT_SECRET']` on line 6 with the copied value in the python file.
12. Save the `album_selector.py`file.

**How to use the program:**
- Run the program. When it is ran for the first time, a new window will open and ask for you to authorize for the program to see some of your user data. Click "Agree". 
- You will be redirected to a Google homepage. Copy the link and paste it into your terminal and press enter. 
- Wait a couple of seconds, and an album will be chosen and printed into the terminal. 

**Notes:**
- When you run the program, a `.cache` file will be created. This stores your access token, the token type, when it expires, and the refresh token.
- If you want to remove access to the program, visit [your account settings](https://www.spotify.com/us/account/apps/) and find the app that mactches the name of the app you created on Spotify's developer website (For example, if my app is called "Album Selector", there would be an app on my account settings page also called "Album Selector"). Click "Remove Access".
