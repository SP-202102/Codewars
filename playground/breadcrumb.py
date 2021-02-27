class urlHandler:
    def __init__(self):
        self.elementList = []
        self.outputHtml = ""

    def splitUrl(self, url, separator ="/" ):
        self.elementList = url.split( separator )
        print("Element List:", self.elementList)
        return


    def buildOutPutUrl(self, separator):
        return( separator.join(self.elementList) )


    def getBcMenu( self, url, separator=" : " ):
        self.splitUrl(url)
        self.outputHtml = self.buildOutPutUrl(separator)
        return ( self.outputHtml )
        
        

def generate_bc(url, separator):
    x = urlHandler()

    outputHtml = ""
    outputHtml = x.getBcMenu( url, separator )

    print(outputHtml) 


# split input / check for python html functions
    # for htmlElement in parser:
    #     print( htmlElement )

    

# make first part "HOME"

# all other parts except last:
    # strip last part?

    # apply rules for short


    #formate output elements incl make them links

# construct output


print(generate_bc( "mysite.com/pictures/holidays.html", " : "))