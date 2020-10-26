#suppose we have a condition that needs to full fill
# we have some attribute also that needs to be conditioned

busfare = 1500
cigarttee = 2000
hangout =  3000

if busfare > 1000 and cigarttee > 1500 and hangout > 2000:
    print("i am sustainable to move around ")


# so how can we make it easy
# here we take a empty list
# suppose we have more than this three condition
# than if we take this if else statement than it will be so long an don't look so pretty


# and put all conditions on it
conditions = [
        busfare > 1000 ,
        cigarttee > 1500 ,
        hangout > 2000
]

# and now we can make it easy using all condition  cz we have to fullfill all condition
# all function take a iterable [list,tuple,set,dict]
if all(conditions):
    print("i am ok ")


# what if we don't need to full fill all condition
# i mean that if we have or keyword

# manually making a if condition using above data

if busfare>2000 or cigarttee>3000 or hangout>2000:
    print("wow i am free")
# here at least one condition is correct
# so if we have many data what can we do then

# taking a list
matches = [
    busfare > 2000 ,
    cigarttee > 3000 ,
    hangout > 2000
]

# any function will help us

if any(matches):
    print("i love myself")

# now this program we make a comprehension that can help us to square the odd number in range 1,10


a = [i**2 for i in range(11) if i%2==1]
print(a)


# in this program we make a  string and reverse it
# so first how can we manually reverse any number

number = 12345
reverese = 0
temp = number

while(temp!=0):
    r = temp%10
    reverese = reverese*10+r
    temp = temp/10

if reverese == number:
    print(True)


# is the hardest things i have ever tastesed

# so now we make it easy
name = 'sakira'[::-1]
print(name)

name2 ='madam'
re = name2.find(name2[::-1])==0
print(re)