'''
regular expression in short re
i am new at it , but i it frekking awesome
if you want to search or any manipulate your data such as a astring
'''
# import re means regular expression
import re

'''name = "shimul islam sabbir"
if re.search("^shimul.*sabbir$",name):
    print("true")
else:
    print("false")

'''

pattern = r"colours"
if re.search(pattern,"red is a colours, i love red colour"):
    print("true")
else:
    print("false")

print("\n")


if re.findall(pattern,"red is a colour, i love red colour"):
    print("true")
else:
    print("false")

print("\n")
print("find all function reatn a list \nso we can keep it in a variable and  later print it ")

print("\n")
Hcolours = re.findall(pattern,"gray is a colour, i love colours , many colours")

print(Hcolours)


# match function
print("\nmatch function")
if re.match(pattern,"black is my favourite colour"):
    print("true")
else:
    print("false")