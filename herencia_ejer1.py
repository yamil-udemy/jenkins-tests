
class Car:

    def __init__(self):
        self.car_banch=input("type in the car branch: ")
        self.car_model=input("type in the car model: ")
        self.car_year=int(input("type in the car year:"))
        self.car_km=int(input("how many kms does it have:"))



class Taxes(Car):
    def taxation(self):
        super().__init__()
        if  self.car_year >= 2010:
            self.tax=self.car_year*2
            print(f"Taxes for the car are: {self.tax}")
        elif self.car_year>=2000 and self.car_year>=2009:
            self.tax=self.car_year*1.5
            print(f"Taxes for the car are: {self.tax}")
        elif self.car_year<=1999:
            self.tax=self.car_year*1.0
            self.tax=self.car_year*1.05
            print(f"Taxes for the car are: {self.tax}")
        if  self.car_model=="civic" or self.car_model=="corolla":
            self.tax=self.tax*1.05
            print(f"class tax for the car are {self.tax} ")
        if self.car_year<=2000:
           print("the car needs an oil change every 6000 kms")
        if self.car_km>=100000:
           print("oil change, oil & air filters, gasoline & transmission filters , are required to be changed")
        elif self.car_km<100000:
           print("oil change, oil & air filters are to be changed")

print("\n")
Taxes().taxation()
#print("\n")
