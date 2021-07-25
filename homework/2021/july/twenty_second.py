#%%
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


#%%
class Vehicle:
    pass


#%%
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


Bus = Vehicle("School Volvo", 180, 12)
print(f"Vehicle name : {Bus.name}, Speed : {Bus.max_speed}, Mileage : {Bus.mileage}")

#%%
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passenger."


class Bus(Vehicle):
    def seating_capacity(self, capacity):
        capacity = 50
        super().seating_capacity()


Bus = Bus("School Volvo", 180, 12)
