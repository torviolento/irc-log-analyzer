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
	posts = []
	time_re = re.compile("<span class=\"time\">([0-9]{2}\:[0-9]{2})</span>")
	#<span class=\"time\">00:01</span> --> ["00:01",]
	usermsg_re = re.compile("<span class=\"msg\"> &lt;(\S*)&gt; (.*)</span>")
	#<span class="msg"> <sensodyne> Mui. people </span> --> ["sensodyne", "Mui. people"]
	othermsg_re = re.compile("<span class=\"msg\">(.*)</span>")
	#sensodyne (sensodyne@asdf.somesite.com) left irc: Connection reset by peer -> ~[storba]
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
	edsort = sorted(users, key=users.__getitem__, reverse = 1) #User with most messages first
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
		edsort = sorted(words, key=words.__getitem__, reverse = 1) #User with most messages first
	for word in edsort:
		if  words[word]< 10: break
		print ("{:20}:- {}".format(word, words[word]))
		
def printAll(data):
	for msg in data:
		try:
			print ("{} | <{}> {}".format(*msg))
		except UnicodeEncodeError: # bubblegum, repair some day
			print ("{} | <{}> {}".format(msg[0].encode("utf-8"),msg[1].encode("utf-8"), msg[2].encode("utf-8")))
			
			
			
			
import re
def find_all(data, find = [], id = 2, startpos = 0): #
	turn = []
	for msg in data:
		for d in find:
			if d in msg[2]:
				turn.append(msg)
	return turn
def search_re_where(data, time = "[0-9]{2}:[0-9]{2}", user = "\w", msg = ".*"):
	matcbox = []
	res = re.compile(time),re.compile(user), re.compile(msg)
	for msg in data:
		for i in (0,1,2):
			if res[i].match(msg[i]) is None:
				break
			elif i == 2: 
				matcbox.append(msg)
	return matcbox

def main():
	data = [["00:00","eeee","aa, bee, cee"],
	["00:12","aaa","aa, bee, cee"],
	["10:12","aaa","ab, bee, cee"],
	["00:00","eee","e"],
	["00:00","eee","aaeh"]]
	for a in search_re_where(a, "00:[0-9]{2}"):
		print(a[0])	
	##data = getDataFromIntternets()
	#parsed = htmlparser(data)
	#countMessages(parsed)	
	#countWords(parsed)
if __name__ == "__main__":
	main()


