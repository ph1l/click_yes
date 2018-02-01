#!/usr/bin/python -u

import time
import urllib2

from HTMLParser import HTMLParser

CHECK_URL = "http://detectportal.firefox.com/success.txt"
CHECK_CONTENT = "success\n"

class HTMLLinkParser(HTMLParser):

    links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            link={}
            for (name, value) in attrs:
                link[name]=value
            self.links.append(link)

parser = HTMLLinkParser()

def check_for_success():

    # Setup our HTTP Client
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())

    req = opener.open(CHECK_URL)
    html = req.read()
    if html != 'success\n': # Success!
        print "!SUCCESS: {} {} [{}]".format(req.getcode(), req.geturl(), len(html))
        parser.feed(html)
        for link in parser.links:
            if link['id'] == 'continue_link':
                req = opener.open(link['href'])
                html = req.read()
                print "CONTINUE:{} {} [{}]".format(req.getcode(), req.geturl(), len(html))

    opener.close()

def main():
    while True:
        check_for_success()
        time.sleep(90)

if __name__ == "__main__":
    main()
