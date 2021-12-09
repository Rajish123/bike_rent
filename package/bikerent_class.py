from datetime import datetime
import json

class BikeRent:
    def __init__(self, royal_enfield, ktm, cf):
        self.royal_enfield = royal_enfield
        self.ktm = ktm
        self.cf = cf

    def display_info(self):
        print(f"Total bikes availabe are:\n Royal Enfield: {self.royal_enfield}\n KTM: {self.ktm}\n Crossfire: {self.cf}")
        return self.royal_enfield, self.ktm, self.cf

    def HourlyBasis(self, bike, num):
        if bike == 1:
            if num < 0:
                print("please use positive integer!")
                return None
            elif num > self.royal_enfield:
                print(f"We have only {self.royal_enfield} royal enfield availabe for rent.")
                return None
            else:
                now = datetime.now()
                print("You have rent bike on Hourly Basis.")
                print(f"You have rented {num} royal enfield.")
                print("You will be charged 5$ per hour.")
                print("Enjoy your ride!")
                self.royal_enfield -= num
                return now

        elif bike == 2:
            if num < 0:
                print("please use positive integer!")
                return None
            elif num > self.ktm:
                print(f"We have only {self.ktm} ktm.")
                return None
            else:
                now = datetime.now()
                print("You have rent bike on Daily Basis.")
                print(f"You have rented {num} ktm availabe for rent.")
                print("You will be charged 5$ per hour.")
                print("Enjoy your ride!")
                self.ktm -= num
                return now

        elif bike == 3:
            if num < 0:
                print("please use positive integer!")
                return None
            elif num > self.ktm:
                print(f"We have only {self.cf} crossfire availabe for rent.")
                return None
            else:
                now = datetime.now()
                print("You have rent bike on Weekly Basis.")
                print(f"You have rented {num} crossfire.")
                print("You will be charged 5$ per hour.")
                print("Enjoy your ride!")
                self.cf -= num
                return now

        else:
            print("Please make sure to choose one bike from above options.")
            return None

    def DailyBasis(self, bike, num):
        if bike == 1:
            if num < 0:
                print("please use positive integer!")
                return None
            elif num > self.royal_enfield:
                print(f"We have only {self.royal_enfield} royal enfield availabe for rent.")
                return None
            else:
                now = datetime.now()
                print("You have rent bike on Daily Basis.")
                print(f"You have rented {num} royal enfield.")
                print("You will be charged 5$ per hour.")
                print("Enjoy your ride!")
                self.royal_enfield -= num
                return now

        elif bike == 2:
            if num < 0:
                print("please use positive integer!")
                return None

            elif num > self.ktm:
                print(f"We have only {self.ktm} ktm.")
                return None

            else:
                now = datetime.now()
                print("You have rent bike on Daily Basis.")
                print(f"You have rented {num} ktm availabe for rent.")
                print("You will be charged 5$ per hour.")
                print("Enjoy your ride!")
                self.ktm -= num
                return now

        elif bike == 3:
            if num < 0:
                print("please use positive integer!")
                return None
            elif num > self.ktm:
                print(f"We have only {self.cf} crossfire availabe for rent.")
                return None
            else:
                now = datetime.now()
                print("You have rent bike on Daily Basis.")
                print(f"You have rented {num} crossfire.")
                print("You will be charged 5$ per hour.")
                print("Enjoy your ride!")
                self.cf -= num
                return now

        else:
            print("Please make sure to choose one bike from above options.")
            return None

    
    def WeeklyBasis(self, bike, num):
        if bike == 1:
            if num < 0:
                print("please use positive integer!")
                return None

            elif num > self.royal_enfield:
                print(f"We have only {self.royal_enfield} royal enfield availabe for rent.")
                return None

            else:
                now = datetime.now()
                print("You have rent bike on Weekly Basis.")
                print(f"You have rented {num} royal enfield.")
                print("You will be charged 5$ per hour.")
                print("Enjoy your ride!")
                self.royal_enfield -= num
                return now

        elif bike == 2:
            if num < 0:
                print("please use positive integer!")
                return None

            elif num > self.ktm:
                print(f"We have only {self.ktm} ktm.")
                return None

            else:
                now = datetime.now()
                print("You have rent bike on Weekly Basis.")
                print(f"You have rented {num} ktm availabe for rent.")
                print("You will be charged 5$ per hour.")
                print("Enjoy your ride!")
                self.ktm -= num
                return now

        elif bike == 3:
            if num < 0:
                print("please use positive integer!")
                return None

            elif num > self.ktm:
                print(f"We have only {self.cf} crossfire availabe for rent.")
                return None

            else:
                now = datetime.now()
                print("You have rent bike on Weekly Basis.")
                print(f"You have rented {num} crossfire.")
                print("You will be charged 5$ per hour.")
                print("Enjoy your ride!")
                self.cf -= num
                return now

        else:
            print("Please make sure to choose one bike from above options.")
            return None

    def CalculateCost(self, request):
        bike_name, num_of_bike, rentalBasis, rentalTime = request
        bill = 0
        if rentalTime and rentalBasis and num_of_bike:
            now = datetime.now()
            rentalPeriod = now - rentalTime
            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * num_of_bike
                
            # daily bill calculation
            elif rentalBasis == 2:
                bill = rentalPeriod.days * 20 * num_of_bike
                print(f"bill is: {bill}")
                
            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * num_of_bike

            print("Thank you for returning bike.")
            print(f"Bike: {bike_name}\n Number of bike rented: {num_of_bike}\n Rent time: {rentalTime}\n Rental Basis: {rentalBasis}\n Total cost: {bill}\n")
            
        else:
            print("opps! you must be mistaken.\n You didin'n rent any bike from our store.")
            return None


    def ReturnBike(self, bike, num):
        if bike == 1:
            self.royal_enfield += num
        elif bike == 2:
            self.ktm += num
        elif bike == 3:
            self.cf += num
        else:
            print("Invalid input")


# saves number of bike available
def write_to_file(owner):
    data = {}
    # if os.path.isfile("bike_information.json"):
    with open("bike_information.json", "r") as f:
        bike_info = json.load(f)
    # else:
        data["royal_enfield"] = owner.royal_enfield
        data['ktm'] = owner.ktm
        data["crossfire"] = owner.cf
        with open("bike_information.json", "w") as f:
            json.dump(data,f)

# saves bike available after user rents a bike
def calulate_num_bike(owner, data):
    data['royal_enfield'] = owner.royal_enfield
    data['ktm'] = owner.ktm
    data['crossfire'] = owner.cf
    with open("bike_information.json", "w") as f:
        json.dump(data,f)

# saves record of customer that rents a bike
def bikerent_record(record_list, cus_info, request):
    bike_type, rentalBasis, num_of_bike, rentalTime = request
    # convert datetime object to string
    rentTime = rentalTime.strftime("%Y-%m-%d, %H:%M:%S") 
    data = {}
    data['name'] = cus_info['name']
    data['contact'] = cus_info['contact']
    data['address'] = cus_info['address']
    data['id'] = cus_info['id']
    data['bike_model'] = bike_type
    data['rental_basis'] = rentalBasis
    data['num_of_bike'] = num_of_bike
    data['rent_date'] = rentTime
    record_list.append(data)
    with open("customer_record.json", "w") as f:
        json.dump(record_list, f)       

        # first commit to github"
