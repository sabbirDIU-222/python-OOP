# abstraction
# abc -> abstract base class

from abc import ABC,abstractmethod

class Btrc(ABC):



    @abstractmethod
    def Text(self):
        pass
    def Phone(self):
        print("we can phone")





class Mycompany(Btrc):
    def call(self):
        pass

    def Text(self,call):
        self.call = call
        print("we can call")
        print("we can textx")







my = Mycompany()
my.call()
my.Text(3)
my.Phone()

'''
polimorphism - many from -> overloading overriding
inheritance  - extends ->  ()
class object
abstraction  - abstract method - > from abc import ABC, abstractmethod
constructor  - def init
encapsulation - capsul - clear @property / property() getter setter
'''
class My:
    _name = "sabbir"
    _id = 1022


    def name_getter(self):
        print("gatter called")
        return self._name


    def name_setter(self,name):
        print("setter called")
        self._name = name

    def id_getter(self):
        print("getter id ")
        return self._id


    def id_setter(self,id):
        print("setter id")
        self._id =id

    '''def del_name(self):
        del self._name
'''
    variable = property(name_getter,name_setter)
    variable1 = property(id_getter,id_setter)



    def __str__(self):
        return self.name + self.id

class You(My):
    yName = "bipasa"
    def __str__(self):
        return self.yName

mamun = You()
mamun.variable = "mamun"
print(mamun.variable)

mamun.variable1 = 1048
print(mamun.variable1)




