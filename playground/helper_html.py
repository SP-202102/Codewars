import html
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


parser = MyHTMLParser()

def generate_bc(url, separator):
    outputHtml = ""
# split input / check for python html functions
    parser.feed(url)
    # for htmlElement in parser:
    #     print( htmlElement )

    elementList = url.split( "/" )

# make first part "HOME"

# all other parts except last:
    # strip last part?

    # apply rules for short


    #formate output elements incl make them links

# construct output
    outputHtml = separator.join(elementList)
    print(elementList)
    print(outputHtml)
    return (outputHtml)



# parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')


print(generate_bc( "mysite.com/pictures/holidays.html", " : "))