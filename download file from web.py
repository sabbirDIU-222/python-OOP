# now this is gonna kind of horrable code
from urllib import request
some_url = "http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv.zip"
# i don't know what is the shit is

def download_file(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    named_url = r'donno.csv'
    fo = open(named_url,"w")
    for line in lines:
        fo.write(line + "\n")
    fo.close()

download_file(some_url)
