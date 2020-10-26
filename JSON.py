'''
JSON -> javascript object notation
so it is a javascript product , but what it fuck to doing here in python
we can make a things to store data in a file or something
'''
# all first we need to import json
import json

# firstly we convert json string to make a python object its like dict

# to converting json to python we need json.load() function

variable = '{"name":"sabbir","age":23,"location" : "dhaka cantonment"}'

convertP = json.loads(variable)
print(convertP)
print(type(convertP)) # its type is dictionary


# convert python to json

dictionary = {"users":{"name":"sabbir","age":"23"},}

# to convert py to json we need to serialized the dictionary

json_str = json.dumps(dictionary,indent=4)
print(json_str)

# by the help of json we can easily handle python file
# and it is important to excel
