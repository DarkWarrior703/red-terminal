#!/usr/bin/env python
import requests
import json
import random
import sys
from pathlib import Path

class Config:
    def __init__(self, data):
        self.username = data['username']
        self.password = data['password']
        self.client_id = data['client_id']
        self.client_secret = data['client_secret']
        self.subreddit = data['subreddit']
        self.user_agent = data['user_agent']
        self.sorting = data['sorting']

#Some global variables
home = Path.home()
stored = []
creds = Config

def config():
    f = open(Path(home, ".config/redterminal/config.json"), "r")
    global creds
    creds = Config(json.load(f))
    if len(sys.argv) > 1:
        creds.subreddit = sys.argv[1]
def evaluate_data(values):
    for i in values['data']['children']:
        data = i['data']
        entry = [data['title'], data['selftext'], data['author'], data['created_utc']]
        stored.append(entry)

def get_data():
    base_url = 'https://www.reddit.com/'
    data = {'grant_type': 'password', 'username': creds.username, 'password': creds.password}
    auth = requests.auth.HTTPBasicAuth(creds.client_id, creds.client_secret)
    r = requests.post(base_url + 'api/v1/access_token',
            data=data,
            headers={'user-agent': creds.user_agent},
            auth=auth)
    d = r.json()

    token = 'bearer ' + d['access_token']

    base_url = 'https://oauth.reddit.com'
    headers = {'Authorization': token, 'User-Agent': creds.user_agent}

    payload = {'t': 'all', 'limit': 200, 'raw_json':1}
    response =  requests.get(base_url + '/r/{0}/{1}'.format(creds.subreddit, creds.sorting), headers=headers, params=payload)
    values = response.json()
    return values

def print_data():
    data = {}
    data[creds.subreddit] = []
    for i in stored:
        data[creds.subreddit].append({
            'title': "'{0}'".format(i[0]),
            'selftext': "'{0}'".format(i[1]),
            'author': "'{0}'".format(i[2]),
            'created': "'{0}'".format(i[3])
            })
    with open(Path(home, ".config/redterminal/data/{0}.json".format(creds.subreddit)), "w") as f:
        json.dump(data, f)

def main():
    config()
    response = get_data()
    evaluate_data(response)
    print_data()

main()
