# #
#       THIS SHOULD BE THE CONTROL FILE
# 
# its main purpose is to open up whatever "main menue" should be displayed
# --- OR ---
# executing the default use case
#
# I am still GUESSING:
# including libraries aso. should be done in Init
# including use cases or modules should be done here
# # 

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

