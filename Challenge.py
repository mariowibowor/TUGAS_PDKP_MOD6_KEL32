from abc import  ABC, abstractmethod

class Vehicle(ABC):

    model = None
    year = None
    color = None

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def __init__(self,model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model

    def go(self):
        print("This " + self.color + " " + self.model + " is driving")
    def run(self):
        print("The " + self.color + " " + self.model + " is running")
    def stop(self):
        print("This " + self.color + " "  + self.model + " is stopped")

class Motorcycle(Vehicle):

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model

    def go(self):
        print("This " + self.color + " " + self.model + " is driving")
    def run(self):
        print("The " + self.color + " " + self.model + " is running")
    def stop(self):
        print("This " + self.color + " " + self.model + " is stopped")

class Bike(Vehicle):

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model

    def go(self):
        print("This " + self.color + " " + self.model + " is driving")
    def run(self):
        print("The " + self.color + " " + self.model + " is running")
    def stop(self):
        print("This " + self.color + " " + self.model + " is stopped")

car = Car("Corvette", 2021, "blue")
print("Car Model : " + car.getModel())
print("Year : " + str(car.year))
print("Color : " + car.color)
car.go()
car.run()
car.stop()
print("---------------------------------------")
motorcycle = Motorcycle("Ducati", 2020, "grey")
print("Motorcycle Model : " + motorcycle.getModel())
print("Year : " + str(motorcycle.year))
print("Color : " + motorcycle.color)
motorcycle.go()
motorcycle.run()
motorcycle.stop()
print("---------------------------------------")
bike = Bike("Brompton", 2022, "black")
print("Bike Model : " + bike.getModel())
print("Year : " + str(bike.year))
print("Color : " + bike.color)
bike.go()
bike.run()
bike.stop()
