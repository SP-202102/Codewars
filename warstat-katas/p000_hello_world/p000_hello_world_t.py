# test cases for 000-hello_world.py
# #
#       THIS SHOULD BE THE TEST CONTROL FILE
#
#       current State: BROKEN, due to rewrite of util base classes
#       main issue is STILL the import-logic
#

# trying in __INIT__ 
# import codewars_test as Test 
# from .. import codewars_test as Test 
#
# Currently Trying: import in __init__.py in root of project -> available for all modules in project
# TODO: cleanup

#import our actual code for testing here
import p000_hello_world as Solution

# this is for codewars compatibility
# insert codewars actual tests below this line
#-----------------------------------------------

Test.assert_equals(Solution.hello_world(), "Hello World!","Text should be \"Hello World!\"")
