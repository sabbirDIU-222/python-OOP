# super class
class student:

      def __init__(self,id,gpa):
        self.id = id
        self.gpa = gpa
        print(f"{self.id}")

#compile time
      def calculategpa(self,waiver):
         self.waiver = waiver
         return self.gpa * self.waiver



# child class
class Male(student):

    def __init__(self,id,gpa,toilet):
        student.__init__(self,id,gpa)
        self.toilet = toilet
        print("toile in 3rd flooor")

#runtime
# static overriden

    def calculategpa(self,waiver,sweiver):
        self.sweiver = sweiver
        self.waiver = waiver
        return waiver * 100 + self.gpa + self.sweiver




m = Male(1048,3.99,3)
print(m.calculategpa(0.5,0.2))


'''class Female(student):
    def __init__(self,id,gpa,commonrooom):
        self.commonroom = commonrooom
        super().__init__(id,gpa)
        print(f"common room is in {self.commonroom}")

f = Female(1022,3.44,4)'''