'''
we work with file and use the dump and load method

1. firstly we need a python dictionary
2. we make a file
3. with open
4. we call json.dump function
5. we convert the python dictionary into a json file
'''

import json

pyton_dict = {
    "name":"sabbir",
    "full name" : "shimul islam sabbir",
    "age":23,
    "maritial status":False,
    "knowledge":[{
        "cse":"computer fundamental",
        "language":["python","java","c","dart","android","flutter"]
    }],
    "home town":"mymensingh"

}
with open('myinfo.txt','w') as myfile:
     json.dump(pyton_dict,myfile,indent=4,sort_keys=True)


