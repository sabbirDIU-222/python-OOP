# so in this program i do a things that can download image from internet
import random
import urllib.request

# now we make a function that can take the image url and can download

def download_from_web(url):
    name = random.randrange(1,1000)
    full_name = str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

download_from_web("http://tinyurl.com/y47elp8p")