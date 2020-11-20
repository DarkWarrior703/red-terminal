#!/usr/bin/env python
import sys
import json
import random
import time
from pathlib import Path

home = Path.home()
subreddit = "dadjokes"
post = []

posted_string = ""

def get_subreddit():
    global subreddit
    try:
        subreddit = sys.argv[1]
    except:
        with open(Path(home, ".config/redterminal/config.json"), "r") as f:
            data = json.load(f)
            subreddit = data['subreddit']

def get_post():
    try:
        f = open(Path(home,".config/redterminal/data/{0}.json".format(subreddit)))
    except:
        sys.exit(str(Path(home,".config/redterminal/data/{0}.json".format(subreddit))) + " does not exist.\nCreate it using redterm regenerate")
    data = json.load(f)
    data = data['{0}'.format(subreddit)]
    number = random.randint(0, len(data) - 1)
    global post
    post = data[number]

def gen_string():
    global posted_string
    created = display_time()
    posted_string = "Posted by u/{0} • {1}".format(post['author'][1:-1], created)

def display_time():
    created = int(post['created'][1:-3])
    actual = int(time.time())
    # Number of seconds of a year
    if actual - created >= 31557600:
        no_years = int(actual-created) // 31557600
        return "{0}y".format(no_years)
    # Number of seconds of a month
    elif actual - created >= 2629800:
        no_months = int(actual-created) // 2629800
        return "{0}mo".format(no_months)
    # Number of seconds of a month
    elif actual - created >= 86400:
        no_days = int(actual-created) // 86400
        return "{0}d".format(no_days)
    elif actual - created >= 3600:
        no_hours = int(actual-created) // 3600
        return "{0}h".format(no_hours)
    else:
        no_minutes = int(actual-created) // 60
        return "{0}m".format(no_minutes)
    # No post are younger than a minute

#Lengths of display blocks
LENGTH = 60
BEGIN = 10
BETWEEN = 5
ACTUAL = 50

def string_text():
    strings = []
    strings.append(center_text("  r/{0}".format(subreddit)))
    strings.append(center_text(" " + posted_string))
    strings.append(center_text(""))
    line = ""
    for i in post['title'][1:-1].split():
        if len(i) + len(line) >= ACTUAL - 5:
            if len(i) > ACTUAL - 5:
                continue
            strings.append(center_text(line))
            line = i
        else:
            line += ' ' + i
    strings.append(center_text(line))
    line = ""
    strings.append(center_text(""))
    strings.append(center_text(""))
    strings.append(center_text(""))
    for i in post['selftext'][1:-1].split():
        if len(i) + len(line) >= ACTUAL - 5:
            strings.append(center_text(line))
            line = i
        else:
            line += ' ' + i
    strings.append(center_text(line))

    return strings

def center_text(string):
    string = " " + string
    payload = (ACTUAL - len(string)) * " "
    string = string + payload
    return string

def display_art():
    print(BEGIN * ' ' + LENGTH * '_')
    print((BEGIN - 1) * ' ' + '/' + LENGTH * ' ' + '\\')
    print((BEGIN - 2) * ' ' + '|' + (BETWEEN + 1) * ' ' + ACTUAL * '_' + (BETWEEN + 1) * ' ' + '|')
    print((BEGIN - 2) * ' ' + '|' + BETWEEN * ' ' + '|' + ACTUAL * ' ' + '|' + BETWEEN * ' ' + '|')
    strings = string_text()
    for i in strings:
        print((BEGIN - 2) * ' ' + '|' + BETWEEN * ' ' + '|' + i + '|' + BETWEEN * ' ' + '|')
    print((BEGIN - 2) * ' ' + '|' + BETWEEN * ' ' + '|' + (ACTUAL) * ' ' + '|' + BETWEEN * ' ' + '|')
    print((BEGIN - 2) * ' ' + '|' + BETWEEN * ' ' + '|' + (ACTUAL) * ' ' + '|' + BETWEEN * ' ' + '|')
    print((BEGIN - 2) * ' ' + '|' + BETWEEN * ' ' + '|' + ACTUAL * '_' + '|' + BETWEEN * ' ' + '|')
    print((BEGIN - 2) * ' ' + '|' + (BETWEEN + 1) * ' ' + ACTUAL * ' ' + (BETWEEN + 1) * ' ' + '|')
    print((BEGIN - 1) * ' ' + '\\' + LENGTH * '_' + '/')
    print((BEGIN + BETWEEN + 4) * ' ' + '\\' + (ACTUAL - 9) * '_' + '/')
def main():
    get_subreddit()
    get_post()
    gen_string()
    display_art()

main()
