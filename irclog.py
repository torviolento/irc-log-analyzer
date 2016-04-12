 #!/usr/bin/python3
 # -*- coding: utf-8 -*-
import urllib.request, re
def getDataFromIntternets():
    url = 'http://irc.testmycode.net/logs/mooc.fi.log.20160311.html'
    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
    text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    return text
def htmlparser(data): #Make more space efficient maybe? 
    """
    Parse messages from data
    """
    posts = []
    
    time_re = re.compile("<span class=\"time\">([0-9]{2}\:[0-9]{2})</span>")
    usermsg_re = re.compile("<span class=\"msg\"> &lt;(\S*)&gt; (.*)</span>")
    othermsg_re = re.compile("<span class=\"msg\">(.*)</span>")
    """
    Compile regular expressions that give wanted data from html
    
    <span class=\"time\">00:01</span> --> ["00:01",]
    <span class="msg"> <sensodyne> Mui. people </span> --> ["sensodyne", "Mui. people"]
    <span class="msg"> senso (senso@domain) left irc: bye </span> --> ["senso (senso@domain) left irc: bye"] 
    
    """
    for row in data.split("\n"):
        if  "<span class=\"time\">" in row and "<span class=\"msg\">" in row:
            time = time_re.search(row).groups()[0]
            if "&lt;" in row and "&gt;" in row: 
                user, msg = usermsg_re.search(row).groups()
                #get normal messages and senders
                posts.append((time,user,msg))
            else:
                othermsg = othermsg_re.search(row).groups()[0]
                #get infomsgs like disconnects
                posts.append((time,"#",othermsg))
    return posts

def countMessages(data):
    """
    Count messages for each user
    """
    users = {}
    for msg in data:
        if msg[1] in users:
            users[msg[1]] += 1
        else:
            users[msg[1]] = 1 
            
    edsort = sorted(users, key=users.__getitem__, reverse = 1) 
    #User with most messages first
    
    for user in edsort:
        print ("{:20}:- {}".format(user, users[user]))
def countWords(data):
    words = {}
    for msg in data:
        for word in msg[2].split(" "):
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
                
        edsort = sorted(words, key=words.__getitem__, reverse = 1)
        #User with most messages first
    for word in edsort:
        if  words[word]< 10: break
        print ("{:20}:- {}".format(word, words[word]))
        
def printAll(data):
    for msg in data:
        try:
            print ("{} | <{}> {}".format(*msg))
        except UnicodeEncodeError: # bubblegum, repair some day
            print ("{} | <{}> {}".format(msg[0].encode("utf-8"),msg[1].encode("utf-8"), msg[2].encode("utf-8")))
            
            
            
            
def find_all(data, find = [], type = 2, startpos = 0): #
    matcbox = []
    for msg in data:
        for d in find:
            if d in msg[type]:
                turn.append(msg)
    return matcbox
    
def re_search(data, time = "[0-9]{2}:[0-9]{2}", user = "\w", msg = ".*"):
    matcbox = []
    res = re.compile(time),re.compile(user), re.compile(msg)
    for msg in data:
        for i in (0,1,2):
            if res[i].match(msg[i]) is None:
                break
            elif i == 2: 
                matcbox.append(msg)
    return matcbox
    
class WKnot():
    def __init__(self,data, links = None):
        if links == None:links = {}
        self.data = data
        self.links = links
    def add(self,link, weight = 1):
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
        return "knot'"+str(self.data) +"' "
def TimeActiveWeb(data, ):
    for msg in data:
        hours,mins = msg[0].split(":")
        re_search(data, time=time)
        
        
def main():
    data = [["00:00","eeee","aa, bee, cee"],
    ["00:12","aaa","aa, bee, cee"],
    ["10:12","aaa","ab, bee, cee"],
    ["00:00","eee","e"],
    ["00:00","eee","aaeh"]]
    printAll(re_search(data, time = "00:[0-9]{2}"))  
    ##data = getDataFromIntternets()
    #parsed = htmlparser(data)
    #countMessages(parsed)    
    #countWords(parsed)
if __name__ == "__main__":
    main()

