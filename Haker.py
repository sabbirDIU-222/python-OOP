import pyshorteners
import random
import urllib.request

def userinput(link):
    name = pyshorteners.Shortener()
    shoert_name = name.tinyurl.short(link)
    return shoert_name


link = input("enter any link here : ")
shortlink = userinput(link)
print(f"the short link looks like {shortlink}")

# now we make download that image
def downloadthatimage(shortlink):
    name1 = random.randrange(1,1000)
    full_name = str(name1)+".jpg"
    urllib.request.urlretrieve(shortlink,full_name)

downloadthatimage(shortlink)