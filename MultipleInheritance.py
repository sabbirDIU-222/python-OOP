'''

when i learn java i always confused abut that why java doesn't support multiple inheritance
so i was found that there was a problem called diamond problem when we make mulitiple inheritance
class a

class b extend a

class c extend a

class d extend c,d  * this is not possible in java

but python makes it awasome


'''

class Students:
    def display(self):
        print("every students should respect their parents and teachers")

class Rahim(Students):
    def badorgood(self):
        print("rahim is a bad guy")

class Karim(Students):
    def badorgood(self):
        print("karim is a good guy")

class Employee(Rahim,Karim):
    pass
    '''
    we don't pass anything in this class and this class is called mulitiple inheritance
    
    '''





employobject = Employee()
employobject.badorgood()
'''
so in Rahim and Karim class we have the same named function 
and in Employ class we don't have any body or any task
so what it gonna print / what the object is gonna print 
it print the almost first value what we pass as the perameter or extended first 
Employ(Rahim,Karim)_ Rahim is in first position so rahim is a bad guy
'''