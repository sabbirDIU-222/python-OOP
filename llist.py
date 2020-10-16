
def addAllNegativenumber(agrument):
    sum =0
    for x in range(1,argument,2):
        if (x%2)==0:
            break
        else:
            sum += x

    print(sum)

argument = int(input("take the range"))
addAllNegativenumber(argument)
