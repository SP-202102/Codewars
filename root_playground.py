#%%
# About cells: cells do really only execute the code within. 
# that means: no imports or stuff in __init__... just the cell
# 
# Simple import test for file project_hello_world in SUBFOLDER projects of current folder
#
# does it not only include hello_world, but also output "Hello World!"?

print("-- 1 --")
#import project_hello_world
# # returns: ModuleNotFoundError

print("-- 2 --")
import my_projects
# # imports and executes __init__.py

print("-- 3 --")
import my_projects.project_hello_world

# from projects import project_hello_world


# returns: ModuleNotFoundError

# # answer: yes it does
print("-- end of cell --")

# %%
print("-- end of file --")
