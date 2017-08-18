from HTMLParser import HTMLParser
# from urllib import parse
from urlparse import urlparse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
    # super().__init__() <<this is not supported in Python 2.7
        HTMLParser.__init__(self)
        self.base_url = base_url
        self.page_url = page_url
    # once we start gathering links we will store it in the set()
        self.links = set()

    def handle_starttag(self, tag, attrs):
        # print(tag)
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = urlparse.urljoin(self.base_url, value)
    # whenever you come across a relative url this home page ^ needs to be stuck on it
                    self.links.add(url)
    # always going to add a properly formatted url to our set of links ^

    def page_links(self):
        return self.links

    def error(self, message):
        pass

# you make a link finder object (which is the html parser)
finder = LinkFinder()
# then you call a function called feed by putting it some HTML and takes care of it automatically
# eventually we will parse out the link of the website
finder.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></'
            'html>')

