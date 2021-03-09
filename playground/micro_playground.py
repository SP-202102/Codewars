#file to try small things isolated

#%%
#
# to test,if importing also means "executing"
#
# # does it not only include hello_world, but also output "Hello World!"?

import hello_world

# # answer: yes it does


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
