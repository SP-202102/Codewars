# #
#       THIS SHOULD BE THE CONTROL FILE
# 
# its main purpose is to open up whatever "main menue" should be displayed
# --- OR ---
# executing the default use case
#
# TODO: fully(!) understand Scoping and visibilty code/function/module/imports/global vs. in classes
# TODO: understanding normal project setup
# TODO: understanding classes and their instantiating in that context
# TODO: understanding the testing frameworks of Python
#
# I am still GUESSING:
# including libraries aso. should be done in Init
# including use cases or modules should be done here
# 
# TODO: update to stupid coding conventions for variable names using underscore instead of CamelCase
# TODO: use: module_name, package_name, ClassName, method_name, ExceptionName, function_name, 
#            GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.

#
#       current State: BROKEN, due to rewrite of util base classes
#       main issue is STILL the import-logic
#

# trying in __INIT__ 
# import codewars_test as Test 

import util

# TODO Part #1 use importlib
# import importlib
# module = importlib.import_module(module_name)

kata = util.warKata()

print("--- 1 ---")
print(kata.List[0])
print(kata.List[1])

print("--- 2 ---")
print(kata.getCode(0))
print(kata.getTest(0))

print("--- 3 ---")
# import currentKata
currentKata = kata.getCode(0)
print("Trying to import: " + currentKata)

import currentKata

# TODO Part #2 use importlib
# importlib.import_module(currentKata)

