from package import bikerent_class, customer_class
import os
from os import name, path
import json
from datetime import datetime



if os.path.isfile("bike_information.json"):
    with open("bike_information.json", "r") as f:
        bike_information = json.load(f)

if os.path.isfile("customer_record.json"):
    with open("customer_record.json", 'r') as f:
        customer_record = json.load(f)
else:
    record = [{"name": "sadf", "contact": "sdf", "address": "fdg", "id": "gfh", "bike_model": 2, "rental_basis": 2, "num_of_bike": 5, "rent_date": "2021-06-01, 19:30:41"}]
    with open("customer_record.json", "w") as f:
        customer_record = json.dump(record, f)
    
if __name__ == "__main__":
    # if no data is provided by owner about no of bike available, it asks
    if not os.path.isfile("bike_information.json"):
        royal_enfield = int(input("Number of royal enfield availabe: "))
        ktm = int(input("Number of ktm bikes availabe: "))
        cf = int(input("Number of crossfire bikes available: "))
        owner = bikerent_class.BikeRent(royal_enfield, ktm, cf)
        bikerent_class.write_to_file(owner)

    # get the no of bike available to provide for customer
    else:
        royal_enfield = bike_information['royal_enfield']
        ktm = bike_information['ktm']
        crossfire = bike_information['crossfire']
        print(f"{royal_enfield} {ktm} {crossfire}")
        owner = bikerent_class.BikeRent(royal_enfield,ktm,crossfire)

    print("\n"*100)        
    print("Welcome to bike rental system".title())
    print("-"*100)        
    print("We have three types of bike available here:")
    print("1.Royal Enfield\n 2.KTM\n 3.Crossfire\n")
    print("-" * 100)
    print("Bike can be rented on following basis:\n")
    print("1.Hourly Basis\n 2.Daily Bais\n 3.Weekly Basis\n")
    print("-" * 100)
    print("What  are you upto?")
    print("1. Bike rent\n 2. Return bike")
    try:
        choice = int(input("Please enter your choice: "))
    except ValueError:
        print("Please use integer")

        
    if choice == 1:
        print("Please fill the following form to rent a bike: ")
        # provide info about customer
        customer = customer_class.customer_info()
        # request customer to provide bike info which they are about to rent
        # returns self.bike_type, self.rentalBasis, self.num_of_bike, self.rentalTime
        request = customer.request_bike() 
        # for Hourly Basis
        if customer.rentalBasis == 1:
            owner.HourlyBasis(customer.bike_type, customer.num_of_bike)
        # for Daily Basis 
        elif customer.rentalBasis == 2:
            owner.DailyBasis(customer.bike_type, customer.num_of_bike)
        # for weekly Basis
        elif customer.rentalBasis == 3:
            owner.WeeklyBasis(customer.bike_type, customer.num_of_bike)
        # after costumer rent a bike, total remaining bike are written on file
        bikerent_class.calulate_num_bike(owner, bike_information) 
        #save record of costumer that rents bike 
        bikerent_class.bikerent_record(customer_record, customer.costumer_info,request)
    
    elif choice == 2:
        customer_id = input("Enter your citizenship id: ")
        # stores id of costumer 
        id_list = []
        for record in customer_record:
            id_list.append(record['id'])
            # check for id in record file
            if record["id"] == customer_id:
                print(f"Name: {record['name']}\n Contact: {record['contact']}\n Address: {record['address']}\n Citizen_id: {record['id']}\n Bike Model: {record['bike_model']}\n Rental Basis: {record['rental_basis']}\n Number of bike rented: {record['num_of_bike']}\n Rented Date:{record['rent_date']}\n")
                rent_date = record.get("rent_date")
                # convert string to datetime object
                date_obj = datetime.strptime(rent_date, '%Y-%m-%d, %H:%M:%S')
                bike_name = record['bike_model'] 
                rental_basis = record['rental_basis']
                num_of_bike =  record['num_of_bike']
                # create object of customer
                customer = customer_class.Customer()
                customer.bike_type = bike_name
                customer.rentalBasis = rental_basis
                customer.num_of_bike = num_of_bike
                customer.rentalTime = date_obj
                # return self.bike_type, self.num_of_bike, self.rentalBasis, self.rentalTime
                request = customer.return_bike()
                owner.CalculateCost(request)
                pay = int(input("Total payment: " ))
                # add number of returned bike
                owner.ReturnBike(bike_name, num_of_bike)
                # saves to file
                bikerent_class.write_to_file(owner)

        if customer_id not in id_list:
            print("Sorry! Your id not found.Please check your id")