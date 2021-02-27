#works, NOT if folder is subfolder of parent folder
#import codewars_test as Test

# not even this works:
from .. import some_dummy_code

print(__file__)

#works, NOT if folder is subfolder of parent folder
import codewars_test as Test

def hello_hello():
    return "hello_hello"

print(Test.assert_equals(hello_hello(),"Hello World!", "result should be \"Hello World!\""))