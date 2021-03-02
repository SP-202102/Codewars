#works, NOT if folder is subfolder of parent folder
#import codewars_test as Test



### TRY: Main Function in Parent as in PC!-PHP
### Just call the requested or Default UseCase 
### -> make it a menue if called directy? 
### Checkout Debugging then


# not even this works:
#from .. import some_dummy_code

print(__file__)

#works, NOT if folder is subfolder of parent folder
#import codewars_test as Test

def hello_hello():
    return "hello_hello"

# So this does not work, because Test is not defined:
# print(Test.assert_equals(hello_hello(),"Hello World!", "result should be \"Hello World!\""))