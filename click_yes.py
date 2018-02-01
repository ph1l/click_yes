#!/usr/bin/python -u
"""
click_yes.py

a script to accept the license agreement to the wifi network on an
ongoing and automated basis. ;-)
"""
import time
import urllib2

from HTMLParser import HTMLParser

CHECK_URL = "http://detectportal.firefox.com/success.txt"
CHECK_CONTENT = "success\n"

class HTMLLinkParser(HTMLParser):
    """
    This HTMLParser sub-class finds all anchors on the fed html so
    we can look for the continue_link.

    this method has a public attribute `links`, a list of dictionaries
    of attributes.
    """
    links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            link = {}
            for (name, value) in attrs:
                link[name] = value
            self.links.append(link)

PARSER = HTMLLinkParser()

def check_for_success():
    """
    This function attempts to load a known URL and verify internet
    access. When appropriate, it searches for the `continue_link`
    and clicks it.
    """

    # Setup our HTTP Client
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    try:
        req = opener.open(CHECK_URL)
    except urllib2.URLError, err:
        print "!!ERROR : {} {} {}".format('ERR', CHECK_URL, str(err))
        return

    html = req.read()
    if html != 'success\n': # Success!
        print "!SUCCESS: {} {} [{}]".format(req.getcode(), req.geturl(), len(html))
        PARSER.feed(html)
        for link in PARSER.links:
            if link['id'] == 'continue_link':
                try:
                    req = opener.open(link['href'])
                except urllib2.URLError, err:
                    print "!!ERROR : {} {} {}".format('ERR', link['href'], str(err))
                    return
                html = req.read()
                print "CONTINUE:{} {} [{}]".format(req.getcode(), req.geturl(), len(html))

    opener.close()

def main():
    """
    void main()
    """
    while True:
        check_for_success()
        time.sleep(90)

if __name__ == "__main__":
    main()
