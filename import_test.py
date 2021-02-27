#works, if folder to be imported is subfolder of current folder
import codewars_test as Test

def hello_hello():
    return "hello_hello"

print(Test.assert_equals(hello_hello(),"Hello World!", "result should be \"Hello World!\""))