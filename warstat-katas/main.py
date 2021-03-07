# this is the control file for all the catas importing 
# its main purpose is to include libraries aso. without modifying paths
import codewars_test as Test
import util

import importlib
#module = importlib.import_module(module_name)

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
importlib.import_module(currentKata)

