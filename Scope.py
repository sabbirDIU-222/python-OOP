'''
we can define variable as global and local
'''

# global variable

mastan = "sabbir"


# local variable
# if any variable is in a method or function it called local variable
def my_local_function():
    mastan = "robiul"
    print(f"alkar mastan hoilo {mastan}")

my_local_function()
#alkar mastan hoilo robiul


print(mastan)
# compiler will contain mastan as two different variable



# globe keyword

def Global_function():
    global x
    x = 200
    print(x)



Global_function()

print(x)

def asolmastan():
    global mastan
    mastan = "mamun"
    print(mastan)

asolmastan()
print(mastan)
