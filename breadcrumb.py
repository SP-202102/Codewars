class urlHandler():
    elementList = []
    def splitUrl(url, separator ="/" ):
        elementList = url.split( separator )
        print("Element List:", elementList)


    def getBcMenu( url, separator=" : " ):
        splitUrl( url)
        return (buildOutPutUrl(separator))
        
        
    def buildOutPutUrl(separator):
        return( separator.join(elementList))



def generate_bc(url, separator):
    outputHtml = ""
    outputHtml = getBcMenu( url, separator )

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