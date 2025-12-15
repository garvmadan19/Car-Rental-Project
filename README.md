# Car-Rental-Project
This is a simple console-based car rental system implemented in Python. It allows customers to rent cars on an hourly, daily, or weekly basis and calculate the corresponding rental bill upon return.

## Features

 - Stock Management: Tracks the total number of cars available in the fleet.
 - Flexible Rental Options: Supports renting cars on three different bases:
     - Hourly 
     - Daily 
     - Weekly 
 - Customer Interaction: Gathers customer details (Name and Phone Number) at startup.
 - Rental Time Tracking: Records the exact time a car is booked.
 - Billing System: Calculates the total rental bill upon car return based on the rental period and basis

## Prerequisites
To run this project, you need to have Python installed on your system.

## How to Use
The application will present a main menu from which you can select an option:
 - Total stock: Displays the number of cars currently available.
 - Rent a car on hourly basis: Prompts for the number of cars and initiates an hourly rental.
 - Rent a car on daily basis: Prompts for the number of cars and initiates a daily rental.
 - Rent a car on weekly basis: Prompts for the number of cars and initiates a weekly rental.
 - Return a car: Calculates and displays the final bill, then returns the cars to stock.
 - Exit: Closes the application.

## Project Structure & Class Details
The project is divided into two main components: main.py and Car_rental_module.py.
### Car_rental_module
This module contains the core logic for the car rental system.
   - Class mycar (Rental Shop)
       - __init__(self, stock=0): Initializes the stock of cars.
       - displaystock(): Prints the current number of cars in stock.
       - rentforhour(self, q): Handles hourly rental logic and updates stock. The rent per hour for one car is 200 INR.
       - rentforday(self, q): Handles daily rental logic and updates stock.
       - rentforweek(self, q): Handles weekly rental logic and updates stock.
       - returnCar(self, request): Calculates the bill and adds cars back to stock.
   - Class customer (Customer)
       - __init__(self): Initializes customer's rental details (cars, rentalBasis, rentalTime, bill).
       - rentacar(): Prompts the customer for the number of cars they wish to rent.
       - returnacar(): Returns the customer's rental details for billing.
### main
   - This script runs the application loop and handles user interaction.
   - It creates instances of mycar (initial stock 100) and customer.
   - It displays the menu and calls the appropriate methods from the classes based on the user's selection.

## Notes
The current billing logic is incomplete/inconsistent across the different rental basis calculations in the provided code. 
Please review and correct the logic in the returnCar method of mycar for accurate billing based on days/weeks.
   - Hourly calculation: $rentalPeriod.seconds/3600\times5\timesnumOfCars
   - Daily calculation: $rentalPeriod.days\times20\timesnumOfCars
   - Weekly calculation: $rentalPeriod.days/7\times60\timesnumOfCars



