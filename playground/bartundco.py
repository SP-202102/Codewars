inputNamelist = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
names = inputNamelist[0:]
#print(names)
names1 = []
blabla = 0


def namelist(names):
    if len(names) > 1:
        # return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
        #                         names[-1]['name'])
        return ' & '.join(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''

print(namelist(inputNamelist))

#names2 = []
#print ("+".join(namelist))
# for val in namelist.itervalues():
#   print(val)
# namelist.values("name")
# for item in namelist:
#   item.values(namelist)
#  list.append(item)
# print(list)
# dict.keys()
# namelist = {'name': 'Bart', 'name': 'Lisa', 'name': 'Maggie'}
# new_list = list(namelist.values())
# print (new_list)
# def namelist):
# !!!!print("Namen:", namelist)
# result = str(namelist).replace("name", "").split(":")
# print(new_list)