# test cases for 000-hello_world.py
import codewars_test as Test
import p000_hello_world as Solution

Test.assert_equals(Solution.hello_world(), "Hello World!","Text should be \"Hello World!\"")