import sys
#Pfad zu codewars_test als systempfad hinterlegen
sys.path.append('D:/coding/')
import codewars_test as Test

def some_function():
    return "test"
print(Test.assert_equals(some_function(),"Hello World!", "result should be \"Hello World!\""))