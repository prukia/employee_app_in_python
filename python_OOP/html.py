from HTMLParser import HTMLParser

# create a subclass and override the handler method
class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.recorddiv = True

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            # print 'start tag'
            for name, value in attrs:
                if name == 'class' and value == 'module-body sa-info':
                    print 'this is the name and value', value
                    if tag == 'li':
                        print 'this is the li', tag

    # def handle_endtag(self, tag):
    #     if tag == "div":
    #         print 'this is the tag', tag
    #
    # def handle_data(self, data):
    #     # if self.recorddiv == True:
    #         print "This is the service address :", data

# instantiate the parse and fed it some HTML
parser = MyHTMLParser()
parser.feed(open('pge_meter_details.html').read())
parser.close()
