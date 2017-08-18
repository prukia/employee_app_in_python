from HTMLParser import HTMLParser

# create a subclass and override the handler method
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag :", tag

    def handle_endtag(self, tag):
        print "Encountered a end tag :", tag

    def handle_data(self, data):
        print "Encountered some data :", data

# instantiate the parse and fed it some HTML
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></'
            'html>')
