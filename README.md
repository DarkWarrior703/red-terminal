# Red terminal
You need Python 3.4+ to run this app.
You cannot see photos with this app, just plain text.
To install the dependencies, just do
```
pip3 install requests
```
or
```
pip install requests
```

This is not like any Reddit apps in terminal. I built this app because I wanted to see a dad joke when I open my terminal. I added the capacity to fetch data from any other subreddit.
You can install it by running make install. It will install it to ~/.local/bin. You advise you to add ~/.local/bin to $PATH if you didn't. The config file and downloaded data is saved at ~/.config/redterminal.
Config files consists of:
- username (Your Reddit username)
- password (Your Reddit password)
- client_id (Create an app at [Reddit](https://www.reddit.com/prefs/apps/). Choose a name, select script and then set redirect url to http://localhost:8080 . You will see the id under "personal use script" after you created the app)
- client_secret (use the secret id that it gives you)
- subreddit (use what subreddit you want. default: r/dadjokes)
- user_agent (choose whatever user agent you want)
- sorting (choose between "new", "top", "controversial", "hot", "rising")

I know that I could have made a single python file. But my scope wasn't to download data every time, because I don't wanna wait 3 seconds for my terminal tostart. I download data once in week.

## Usage:
- redterm display (subreddit) - displays the art work, if you give it a subreddit, it will display data from that subreddit.json file, otherwise it will use the one found in config.json
- redterm regenerate (subreddit) - downloads new data, if you give it a subreddit, it will download data for that subreddit, otherwise it will use the one found in config.json

### Wish you have a nice day!
