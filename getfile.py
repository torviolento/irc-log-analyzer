import urllib.request, re
url = 'http://irc.testmycode.net/logs/mooc.fi.log.20160311.html'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
text = text.encode('utf-8')
text = str(text)
with open('testfile', 'w') as file_:
    file_.write(str(text))