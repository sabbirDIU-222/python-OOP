'''
in Java what we learn in Abstruct class
An abstract class contain one or more abstruct method or any default method also
and we can not create any instance of abstract class
but abstract class can have subclass and those subclass must implement the abstract method

in python
same as java but pythod does not have any it's own abstract functionality
python abstract class contain from a module and we implement it
and overall the same

'''

# how can not we make abstract

class Abstractclass:
    def __init__(self):
        print("this is abstract class")

    def abstractfunction(self):
        pass

class subclass(Abstractclass):
    pass

objectofsub = subclass()
objectofsub.abstractfunction()

'''so this program print this
this is abstract class

but does it require all that things what have a abstract class need 
NO!!
even this Abstract class can make or instantiated
'''
# objectofabs = Abstractclass()

'''
        ****** so fuck all that things what you need to do is 
        make a class and import abstract base class module 
        from abc import ABC ,abstractmethod
suppose we have a class name telecommunication
or telePhon
and we the users can make messages 
so what type of messages we sent we don't know or don't share with the call center



'''


from abc import ABC, abstractmethod

class TelephonY(ABC):
    @abstractmethod
    def messages(self):
        print("thelephony can access your device")

class UserOne(TelephonY):
    def makephone(self):
        print("phone is ringing")

    def messages(self):
        print("your messages is ready to sent")


sabbir = UserOne()
sabbir.makephone()
sabbir.messages()

'''
we still can not create abstract class instance


ob = TelephonY()
ob.messages()'''


