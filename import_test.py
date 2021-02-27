#works, if folder to be imported is subfolder of current folder 
# and package; the actual code file has to be imported in the __init__.py in that package, 
# if the codefile is not the same name as the folder (did not check this part)
import codewars_test as Test

def hello_hello():
    return "hello_hello"

print(Test.assert_equals(hello_hello(),"Hello World!", "result should be \"Hello World!\""))