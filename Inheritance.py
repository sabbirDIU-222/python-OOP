'''public class student{

    public student(){
       system.out.println("this is default constructor")
}
  public void print(){
   system.out.println("this print")
}

}
public class student1 extends student{

        student1(){
        super()
        system.out.println("")
}

}

so this is the way we extendes or inheritance any class in java

'''
# inheritance in python

class Student:
    def __int__(self,id,section):
        self.id = id
        self.section = section
        print("this is in Student class")

    def print(self):
        print(f"the id is {self.id} and section is {self.section}")


class student1(Student):
    def __init__(self,name="rashed"):
        self.name=name
        #Student.__int__(self,id,section="d")

        print(f"{self.name}")



karim  = student1("karim")
# when i use constructor in child class that means we are now not able to access the parent class constructor
# to access the parent calss constructor we need to define or call the parent class constructor
# we can use parent class name or manually call super

# again create a class that inherited Student class and it have it's own constructor

class student2(Student):
    def __init__(self,id,section,graduation):
         Student.__int__(self,id,section)
         print("this is student2 class ")
         self.gradution = graduation

    def print(self):
        print(f"so he passe in year {self.gradution}")



rahim = student2(222,"y",2022) # runtime
rahim.print()






class Man():
    def __init__(self,id,name):
        self.id = id
        self.name = name
        print(f"name : {self.name} id is {self.id}")



class Women(Man):
    def __init__(self,id,name,sex):
        Man.__init__(self,id,name)
        self.sex = sex
        print(f" sex is {self.sex}")


ritu = Women(2,"ritu","F")
e = Man(33,"aa")

