# test cases for 000-hello_world.py

# 
from .. import codewars_test as Test # <- does not work, would require fixing path
# alternate solution: import in __init__.py in root of project -> available for all modules in project

#import our actual code for testing here
import p000_hello_world as Solution

# this is for codewars compatibility
# insert codewars actual tests below this line
#-----------------------------------------------

Test.assert_equals(Solution.hello_world(), "Hello World!","Text should be \"Hello World!\"")