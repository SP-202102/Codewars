# #
#       THIS IS JUST FOR TESTING HOW AND IF THE IMPORTS WORK
#
# # 

#
#       current State: 
#
# WOULD work NOT, if folder is subfolder of common parent folder with the folder to include
#
#import codewars_test as Test



### TRY: Main Function in Parent as in PC!-PHP
### Just call the requested or Default UseCase 
### -> make it a menue if called directy? 
### Checkout Debugging then


# not even this works:
#from .. import some_dummy_code

print(__file__)

def hello_hello():
    return "hello_hello"

#
#       SUB ISSUE 1
#
# see MAIN ISSUE
# leads to: "Test" is not defined
#
# print(Test.assert_equals(hello_hello(),"Hello World!", "result should be \"Hello World!\""))
#
#       /SUB ISSUE 1