#how to short any link
import pyshorteners


user_link = input("enter the link : ")

name = pyshorteners.Shortener()
sorter = name.tinyurl.short(user_link)
print(f"the shorter link is : {sorter}")
