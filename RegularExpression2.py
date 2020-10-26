'''
as we learn rigth now that a regular expression can help us to find some
or find a patter from a brunch of string
'''

import re

txt = "i am a very hones persion , i love my country"
variable = re.search("persion",txt)

if variable:
    print(variable.start()) # start function will return the first index number of our desire pattern
    print(variable.end())   # end function will return the last index number of our desire pattern
    print(variable.span())  # span function will return the first and last index of our desire pattern
    #print(variable.string)  # return the desire string
    #print(variable.group()) # return the part of the string

# so match function declare the first string

'''
in python we regularly use split function but we don't know that it is a part of regular expression
it is a awesome things , it spilt or divided the things and return a list 
'''
text = "i am shimul"
mathes = re.split("\s",text)
print(mathes)

#['i', 'am', 'shimul']

mSub = re.sub("\s","--",text)
print(mSub) # i--am--shimul