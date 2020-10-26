'''
can we make change any function without touching it
yes i
we can
in python everything is object

'''
def division(a,b):
    print(a/b)

division(2,4) # 0.5
# but we don't want this
# we want that we swap the value if the value is a is less than b

# remeber we don't touch the division function

'''def division(a,b):
    if a<b:
        a,b = b,a
    print(a/b)

'''
# so the concept decorator comes , decoretor we use in property decorator in encapsulation

def decorate_division(func): # it takes a function
    def div(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return div

division1 = decorate_division(division)
division1(2,8)

'''
Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
Functions can be defined inside another function and can also be passed as argument to another function.
'''


def deco(func):

    def inner():
        print("before function exicution")
        func()
        print("after function exicution")

    return inner()



def a_nameless_boy():
    print("i have nothing to show the world")




a_nameless_boy = deco(a_nameless_boy)

