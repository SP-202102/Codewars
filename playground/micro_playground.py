#file to try small things isolated

#%%
print("hello cell world")
# %%


def splitUrl( url, separator ="/" ):
        elementList = url.split( separator )
        print("Element List:", elementList)
        return


splitUrl("abc/def", "/")
splitUrl(url="asd/fgh")

class theMightyClass:
    def bla( self ):
        splitUrl("huga/huga/haga")
        

x = theMightyClass()
x.bla( )
