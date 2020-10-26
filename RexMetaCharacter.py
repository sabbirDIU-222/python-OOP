''' there are some meta character in regular expression suppose
we need to know a specifiq word to find then the meta character will help us
'''
import re
text = "today is a very cloudy day, i am very much interersted to jump outside,59"
mathces =re.findall("[b-i]",text) # find all lower case character between a to z
print(mathces)


# \d
res = re.findall("\s",text) # \s print white space
res1 = re.findall("\d",text)

print(res)
print(res1)

# start with

res2 = re.findall("^today",text) # ^
if res2:
    print(f"yes this txt start with {res2}")
else:
    print("false")

#end with
x = re.findall("9$",text) # $
if x:
    print(f"yes end with {x}")
else:
    print("not end with")

# exactly the specified number occourance

u = re.findall("al{2}",text)
if u:
    print(f"don not what happen {u}")
else:
    print("not end with")


