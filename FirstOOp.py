class student:
    gpa = " "
    id = " "

    def __init__(self,id,gpa):
        self.id = id
        self.gpa = gpa

    def __int__(self,id):
        self.id = id


    def printvalue(self):
        print(f"id : {self.id} get gpa : {self.gpa}")



object1 = student(1037,3.22)

object1.printvalue()

object2 = student(1045,3.32)

object2.printvalue()

object3 = student(2322,3.23)

object3.printvalue()

object4 = student(12,33)

object4.gpa = 4
object4.id = 1202

object4.printvalue()

