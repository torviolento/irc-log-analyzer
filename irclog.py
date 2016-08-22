#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import re
from datetime import datetime
from datetime import timedelta


def get_data_from_internet():
    url = 'http://irc.testmycode.net/logs/mooc.fi.log.20160311.html'
    response = urllib.request.urlopen(url)
    data = response.read()
    # a `bytes` object
    text = data.decode('utf-8')
    # a `str`; this step can't be used if data is binary
    return text


def print_by_largest(stuff, limit=0):
    for key in sorted(stuff, key=stuff.__getitem__, reverse=1):
        if limit != 0 and stuff[key] < limit:
            break
        print("{:20}:- {}".format(str(key), stuff[key]))


def html_parser(data):
    # Make more space efficient maybe?
    """
    :param data: html file to parse
    :type data: str
    Parse messages from data
    :returns:None
    :rtype: None
    """
    posts = []
    
    time_re = re.compile("<span class=\"time\">([0-9]{2}\:[0-9]{2})</span>")
    user_msgs_re = re.compile("<span class=\"msg\"> &lt;(\S*)&gt; (.*)</span>")
    # other_msgs_re = re.compile("<span class=\"msg\">(.*)</span>")
    
    """
    Compile regular expressions that give wanted data from html
    
    <span class=\"time\">00:01</span>
    --> ["00:01",]

    <span class="msg"> <sensodyne> Mui. people </span>
    --> ["sensodyne", "Mui. people"]

    <span class="msg"> senso (senso@domain) left irc: bye </span>
    --> ["senso (senso@domain) left irc: bye"]
    
    """
    
    for row in data.split("\n"):
        if "<span class=\"time\">" in row and "<span class=\"msg\">" in row:
            time = time_re.search(row).groups()[0]
            if "&lt;" in row and "&gt;" in row: 
                user, msg = user_msgs_re.search(row).groups()
                # get normal messages and senders
                posts.append((time, user, msg))
            else:
                pass
                # other_msg = other_msgs_re.search(row).groups()[0]
                # get info_msgs like disconnects

                # posts.append((time,"#",other_msg))
    return posts


def count_messages(data):
    """
    :param data: parsed data
    :type data: list
    Count messages for each user
    """
    users = {}
    for msg in data:
        if msg[1] in users:
            users[msg[1]] += 1
        else:
            users[msg[1]] = 1 
            
    print_by_largest(users, 10)


def count_words(data):
    words = {}
    for msg in data:
        for word in msg[2].split(" "):
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    # User with most messages first
    for word in sorted(words, key=words.__getitem__, reverse=1):
        if words[word] < 10:
            break
        print("{:20}:- {}".format(word, words[word]))


def count_word_pairs(data):
    words_pairs = {}
    for msg in data:
        words = msg[2].split(" ")
        for i in range(0, len(words)-2):
            key = frozenset((words[i], words[i+1]))
            if key in words_pairs:
                words_pairs[key] += 1
            else:
                words_pairs[key] = 1
    print_by_largest(words_pairs, 4)


def print_all(data):
    for msg in data:
        try:
            print("{} | <{}> {}".format(*msg))
        except UnicodeEncodeError:
            # bubblegum, repair some day
            print("{} | <{}> {}".format(msg[0].encode("utf-8"),
                  msg[1].encode("utf-8"), msg[2].encode("utf-8")))


def find_all(data, find=[], dtype = 2, ):
    matchbox = []
    for msg in data:
        for d in find:
            if d in msg[dtype]:
                matchbox.append(msg)
    return matchbox
    

def re_search(data, time="[0-9]{2}:[0-9]{2}", user="\w", msg=".*"):
    """
    :param data: Data to handle
    :param time: Regexp to match time
    :param user: Regexp to match nick
    :param msg: Regexp to match message
    :return: List of matches
    """

    matchbox = []
    res = re.compile(time), re.compile(user), re.compile(msg)
    """test for each part, time, nick and message if regexps match"""

    for msg in data:
        for i in (0,1,2):
            # res[0] =  regexp for time, msg[0] is send time
            if res[i].match(msg[i]) is None:
                # if regexp didn't match, break
                break
            elif i == 2:
                # else if this is last part of message (actual message),
                matchbox.append(msg)
    return matchbox
    

class WKnot:
    next_id = 0
    
    def __init__(self, data, links=None):
        if links is None:
            links = {}
        self.data = data
        self.links = links
        self.id = self.next_id
        self.next_id += 1
        
    def add(self, link, weight = 1):
        if self == link:
            return
        if link not in self.links:
            self.links[link] = weight
        else:
            self.links[link] += weight
        if self in link.links:    
            if self.links[link] != link.links[self]:
                link.add(self, abs(self.links[link] - link.links[self]))
            
    def __str__(self):
        return "knot'"+str(self.data) + "' "


def time_active_web(data, ):
    #todo: do

    # Add 1 day
    print (datetime.now() + timedelta(days=1))

    # Subtract 60 seconds
    print( datetime.now() - timedelta(seconds=60))

    # Add 2 years
    print( datetime.now() + timedelta(days=730))

    # Other Parameters you can pass in to timedelta:
    # days, seconds, microseconds,
    # milliseconds, minutes, hours, weeks

    # Pass multiple parameters (1 day and 5 minutes)
    print (datetime.now() + timedelta(days=1,minutes=5))
        

def make_activity_web_by(data):
    for msg in data:
        pass


def main():

    data = get_data_from_internet()
    parsed = html_parser(data)

    count_word_pairs(parsed)

    # Lisää päivät aina joka kerta ku avaat uuden päivän aika
if __name__ == "__main__":
    main()
