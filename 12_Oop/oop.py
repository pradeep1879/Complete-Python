# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def fullName(self):
#         return f"{self.brand} {self.model}"


# class TeslaElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

# my_car = Car("Toyota", "Corolla")

# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())

# my_new_car = Car("TATA", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)

# new_tesla = TeslaElectricCar("Tesla", "Model S", "80kWh")
# print(new_tesla.brand)
# print(new_tesla.fullName())


#Ques.Modify the Car class to encapsulate the brand attribute, making it private, and provide a 
#     getter mehtod for it

# class NewCar:
#     def __init__(self, brand, model):
#         self.__brand = brand    #__ to make it private
#         self.model = model
    
#     def get_brand(self):
#         return self.__brand + " !"
    
#     def fullName(self):
#         return f"{self.__brand} {self.model}"
    
# nice_car = NewCar("Honda", "Amaze")
# print(nice_car.get_brand())
# print(nice_car.fullName())
# print(nice_car.__brand)

#Ques.Demonstrate Polymorphism by defining a method fuel_type in both Car and ElectriCar classes, but 
#     with different behaviors.
    
class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def fullName(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol and diesel"


class ElectricCar(Car):
    
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        

    def fuel_type(self):
        return "Electric Charge"
    
audi_electric = ElectricCar("Audi", "Q5", "80kWh")
print(audi_electric.fuel_type())

mahindra_fuel = Car("Mahindrea", "XUV")
print(mahindra_fuel.fuel_type())


#Ques.Add a class variable to Car that keeps track of the number of cars created.

print(Car.total_car)

#Ques.Add a static method to the Car class that returns a general description of a car.(decorator)

#Ques.Demonstrate the use of isinstance() to checkif my_tesla is an instance of Car and ElectricCar.
print(isinstance(audi_electric, Car))
print(isinstance(audi_electric, ElectricCar))

#Ques.Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating
#      multiple inheritance

class Battery():
    def battery_info(self):
        return "This is battery"

class Engine():
    def engine_info(self):
        return "This is engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass


my_second_car = ElectricCarTwo("Tesla", "Model S")
print(my_second_car.battery_info())
print(my_second_car.engine_info())