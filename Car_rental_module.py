#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime

class mycar:
    
    def __init__(self,stock=0):

        self.stock = stock

    def displaystock(self):
        

        print("Total cars in stock: ",self.stock)
        return self.stock

    def rentforhour(self, q):
        
        if q <= 0:
            print("!Enter the positive value!")
            return None
        
        elif q > self.stock:
            print("!Value exceed the cars in stock!")
            return None
        
        else:
            self.stock=self.stock-q
            print("Remaining cars available in stock: ",self.stock)
            now=datetime.datetime.now()
            print("You have booked your car(s) on ",now)
            print("Rent per hour for one car is 200(INR).")
            print("We hope that you will enjoy our service.")
            
            return now      
     
    def rentforday(self, q):
        
        if q <= 0:
            print("!Enter the positive value!")
            return None

        elif q > self.stock:
            print("!Value exceed the cars in stock!")
            return None
    
        else:
            self.stock=self.stock-q
            print("Remaining cars available in stock: ",self.stock)
            now=datetime.datetime.now()
            print("You have booked your car(s) on ",now)
            print("Rent per day for one car is 600(INR).")
            print("We hope that you will enjoy our service.")
            
            return now
        
    def rentforweek(self, q):
        
        if q <= 0:
            print("!Enter the positive value!")
            return None

        elif q > self.stock:
            print("!Value exceed the cars in stock!")
            return None        
        
        else:
            self.stock=self.stock-q
            print("Remaining cars available in stock: ",self.stock)
            now=datetime.datetime.now()
            print("You have booked your car(s) on ",now)
            print("Rent per week for one car is 1000(INR).")
            print("We hope that you will enjoy our service.")
            
            return now
    

    
    def returnaftercar(self, request):
        
        rentalTime, rentalBasis, numOfCars = request
        bill = 0

        if rentalTime and rentalBasis and numOfCars:
            self.stock += numOfCars
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
        
            if rentalBasis == 1:
                print("You have returned the car(s) on",now)
                bill = rentalPeriod.seconds / 3600 * 200 * numOfCars
                print(f"YOUR TOTAL IS: {bill} Rupees")
                print("!Hope you enjoyed our service!")
            
            elif rentalBasis == 2:
                print("You have returned the car(s) on",now)
                bill = rentalPeriod.seconds / (3600*24) * 600 * numOfCars
                print(f"YOUR TOTAL IS: {bill} Rupees")
                print("!Hope you enjoyed our service!")
            
            elif rentalBasis == 3:
                print("You have returned the car(s) on",now)
                bill = rentalPeriod.seconds / (3600*24*7) * 1000 * numOfCars
                print(f"YOUR TOTAL IS: {bill} Rupees")
                print("!Hope you enjoyed our service!")
                
            return bill
        else:
            print("Are you sure you rented a car with us?")
            return None



class customer:

    def __init__(self):
        
        self.cars = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
 
    def rentacar(self):                      
        cars=int(input("Enter the number of car(s) you want to rent: "))

        if cars < 1:
            print("!INVALID INPUT.Enter the positive value!")
            return -1
        else:
            self.cars = cars
        return self.cars
     
    def returnacar(self):
        if self.rentalBasis and self.rentalTime and self.cars:
            return self.rentalTime, self.rentalBasis, self.cars  
        else:
            return 0,0,0

