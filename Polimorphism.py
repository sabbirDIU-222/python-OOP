'''
polimorphism is the same shit what we learn in java

many forms or many phrms

it's like your gf or bf same named but different characteristic

We may call a overriden method as a polimorphic example

overloading can also be , but that time it will called static polimorhisom


'''

# see in built in function  of python

print("length of a string ", len("md shimul islam sabbir"))
print("length of a list ", len([1, 2, 3, 4, ]))

'''
same named but why it takes different parameter
so the len function have different character and its called polimorphism
'''


# polimorphism in class

class Men:
    def run(self):
        print("a men can run faster than a lady")

    def concertation(self):
        print("a men concern is lousy than a lady ")


class Women:
    def run(self):
        print("a women can not run faster than a men")

    def concertation(self):
        print("a women concern is sharp than a men ")



def func(obj):
    obj.run()
    obj.concertation()



sabbir = Men()
moon = Women()

print(func(sabbir))
print(func(moon))


# polimorphism in inheritance

class Vehicle:
    def __init__(self):
        print("all vehicle should contain the traffic rule ")

    # in python we can not use mulitiple in it

    def speed(self):
        pass


class Bus(Vehicle):
    def speed(self, s):
        self.s = s
        print("bus speed sould be ",s * 40/100, "in busy road")

hanif = Bus()
hanif.speed(40)

# polimorphism in abstract class
print("\n")
print("")
from abc import ABC,abstractmethod
class School(ABC):
    @abstractmethod
    def rules(self):pass

class CPSCM(School):
    def rules(self):
        print("our rule is like cadet college rule \n"
              "we make our students strong as hero of nation")

cp = CPSCM()
cp.rules()


# end

'''
length of a string  22
length of a list  4
a men can run faster than a lady
a men concern is lousy than a lady 
None
a women can not run faster than a men
a women concern is sharp than a men 
None
all vehicle should contain the traffic rule 
bus speed sould be  16.0 in busy road



our rule is like cadet college rule 
we make our students strong as hero of nation

'''