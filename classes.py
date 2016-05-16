from datetime import timedelta, strptime, datetime
t1 = datetime.strptime('01:12','%H:%M')
t2 = datetime.strptime('18:59','%H:%M')
print("t1 - t2 = {}, t1 - t2 = {}".format(t1 - t2, t1 - t2))
import urllib

class AsdfData:

    BASE = "http://irc.testmycode.net/logs/mooc.fi.log.{}.html"

    FORMAT = "%Y%m%d"
    START = strptime("20120127", FORMAT)
    END = datetime.now()
    current = START

    def __init__(self):
        self.i = 0
        self.data = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.i:
            pass
        elif 2:
            self.CURRENT = self.current + timedelta(days=1)
            url = self.BASE.format(self.current.strftime(self.FORMAT))
            self.data = self.get_data_from_intternets(url)
        else:
            raise StopIteration("penis,", penis=100)

    @staticmethod
    def get_data_from_intternets(self, url):
        # url = 'http://irc.testmycode.net/logs/mooc.fi.log.20160311.html'
        response = urllib.request.urlopen(url)
        data = response.read()
        # a `bytes` object
        text = data.decode('utf-8')
        # a `str`; this step can't be used if data is binary
        return text

    @staticmethod
    def parse_html(self, data):
        # Make more space efficient maybe?
        """
        :param data: html file to parse
        :type data: str
        Parse messages from data
        :returns: List of data in format [[time, user, message], ... ]
        :rtype: list
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
                    # get normal messages and senders
                    posts.append((time,user,msg))
                else:
                    othermsg = othermsg_re.search(row).groups()[0]
                    # get infomsgs like disconnects
                    posts.append((time,"#",othermsg))
        return posts

    print(())
