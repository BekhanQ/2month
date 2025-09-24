class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car is starting")

class ElectricCar(Vehicle):
    def start(self):
        super().start()
        print("ElectricCar is starting")

class Tesla(ElectricCar, Car):
    def start(self):
        super().start()
        print("Tesla is ready")

Tesla().start()