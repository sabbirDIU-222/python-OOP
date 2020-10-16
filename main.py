# we need to some imported library
# i have already install it ,
import pyshorteners
import random
import urllib.request

# first take the input
yourlink = input("enter your link address : ")

# give a name of it

name = pyshorteners.Shortener()
sname = name.tinyurl.short(yourlink)

print(f"your shortcut link is : {sname}") # interpolation

# now we make a function that can take any url and download it (((imnage)))

def downloadimage(url):
    iname = random.randrange(1,1000)
    sname = str(iname)+".jpg"
    urllib.request.urlretrieve(url,sname)

# we are already done


downloadimage(sname)
# sname is the link what we already short in tinyurl methology]



# lets take a img address

# image name in 1 1000 range


























































'''import pyshorteners
import random
import urllib.request

yourlink = input("enter your large link")
fname = pyshorteners.Shortener()
shortname = fname.tinyurl.short(yourlink)

print(f"your short cut link name is : {shortname}")

def download(url):
    name = random.randrange(1,1000)
    oname = str(name)+".jpg"
    urllib.request.urlretrieve(url,oname)


download(shortname)
'''