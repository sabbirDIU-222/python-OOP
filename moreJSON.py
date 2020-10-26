'''javascript object notation'''
import json

person_str = '''{ "person": [{"name":"shimul islam sabbir",
                              "age":23,
                              "married":false},
                             {"name":"kamrul hasan",
                             "age":21,
                             "married":true},
                             {"name":"rashed",
                             "age":34,
                             "married":false}], 
                             
                             "company":"Dream tech"}'''

# we convert it an pythoon dictionary

person_dict = json.loads(person_str)
'''for i in person_dict['person']:
    print(i)

   '''

back_json_str = json.dumps(person_dict,indent=4,sort_keys=True)
print(back_json_str)

'''
**************************************************
load and dump
'''

