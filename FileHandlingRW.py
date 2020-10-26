fw = open("myfail.txt","w")
fw.write("hello this is sabbir and this is my second time \n")
fw.write("to write file with pyton")
fw.close()


try:
    fr = open("myfil.txt", "r")
    readfile = fr.read()
    print(readfile)
    fr.close()
except:
    print("file is not found")








