class Vehicle:
    def __init__(self,busid,capacity):
        self.busid = busid
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        total = super().fare()
        total += total * 10/100
        return total


school = Bus(111,50)
result = school.fare()
print(result)
print(issubclass(Bus,Vehicle))