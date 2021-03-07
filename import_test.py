# #
#       THIS IS JUST FOR TESTING HOW AND IF THE IMPORTS WORK
#
# # 

#
#       current State: 
#
# WOULD work, if folder to be imported is subfolder of current folder 
# and package; the actual code file has to be imported in the __init__.py in that package, 
# if the codefile is not the same name as the folder (did not check this part)

#
#       MAIN ISSUE
#
# # THIS DOES NOT WORK, BECAUSE THERE ARE ONLY PROJECTS UNDER THIS FOLDER
# EACH POSSIBLY USING DIFFERENT TEST-LIBS
#
# import codewars_test as Test
#
#       /MAIN ISSUE

def hello_hello():
    return "hello_hello"

#
#       SUB ISSUE 1
#
# see MAIN ISSUE
# leads to: "Test" is not defined
#
# print(Test.assert_equals(hello_hello(),"Hello World!", "result should be \"Hello World!\""))
#
#       /SUB ISSUE 1