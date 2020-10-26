'''
in java we use getter setter for the concept encapsulation and we did it very well for our private
property
but now in python it seems like different but we can handle it very well

firstly we make a class and put random get set function let seee
'''
class Employee:
    def __init__(self):
        self.id = 0

    def get_id(self):
        return self.id

    def set_id(self,id):
        print("set called")
        self.id = id

misu = Employee()
print(misu.set_id(1037))
misu.get_id()
print(misu.id)

# in  this avobe program the get id and set id concept is not getter and setter
# it is like general function We can change the value any time

misu.id = 333
print(misu.id) # 333 see


#********************************************************************************************************************


# now the concept encapsultion
# in python we can use normal function like getter and setter but for orginally does it
# we need property class object
# so it can be doen in two way


# property function ** take four perameter ___ get,set,del,doc

class Student:
    def __init__(self):
        self.phone = None

    def get_phone(self):
        print("getter is called")
        return self.phone

    def set_phone(self,phonenum):
        if(phonenum<0):
            raise ValueError("your number is incorrect")
        print("setter is called")
        self.phone = phonenum

    def del_num(self):
        del self.phone

    student = property(get_phone,set_phone,del_num)


student1 = Student()
student1.student = 12323
print(student1.student)


# now the another wway

# property setter and getter
# property decorator

class Islam:
    def __init__(self):
        self._iman = 3


 # we have need the same name for setter getter

    @property
    def Iman(self): # Iman same as setter name
        return self._iman



    @Iman.setter
    def Iman(self,eman):
        if(eman!=5):
            raise Exception("your eman is not in right way @ pray 5 watta salat")
        print("set iman method called")
        self._iman = eman


    @Iman.deleter
    def Iman(self):
        del self._iman



muslim = Islam()
muslim.Iman = 5
print(muslim.Iman)
