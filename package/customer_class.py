import json
from datetime import datetime 


class Customer:
    def __init__(self):
            self.bike_type = 0
            self.rentalBasis = 0
            self.num_of_bike = 0
            self.rentalTime = 0

    def customer_information(self, **kwargs):
        self.name = kwargs.get("name")
        self.contact = kwargs.get("contact")
        self.address = kwargs.get("address")
        self.id = kwargs.get("id")
        
        self.costumer_info = kwargs

    def update_info(self, **kwargs):
        self.costumer_info = {**self.costumer_info, **kwargs}

    def set_address(self,address):
        self.address = address
        self.update_info(address = address )
        
    def get_address(self):
        return self.address

    def set_contact(self, contact):
        self.contact = contact
        self.update_info(contact = contact)

    def get_contact(self):
        return self.contact

    def request_bike(self):
        try:
            bike_type = int(input("Which of the above bike brand you want to hire: "))
            rentalBasis = int(input("On what basis you want to rent a bike: "))
            num_of_bike = int(input("How many bike you want to rent: "))
        except ValueError:
            print("Invalid input.Please use integer!")
        else:
            self.bike_type = bike_type
            self.rentalBasis = rentalBasis
            self.num_of_bike = num_of_bike
            self.rentalTime = datetime.now()
            return self.bike_type, self.rentalBasis, self.num_of_bike, self.rentalTime

    def return_bike(self):
        if self.bike_type and self.rentalBasis and self.rentalTime and self.num_of_bike:
            return self.bike_type, self.num_of_bike, self.rentalBasis, self.rentalTime
        else:
            return 0,0,0,0


# ask customer to provide their information
def customer_info():
    name = input("Enter your name: ")
    contact = input("Enter your contact no: ")
    address = input("Enter your current address: ")
    id = input("Enter your citizenship id number: ")
    customer = Customer()
    customer.customer_information(name = name, id = id)
    customer.set_address(address)
    customer.set_contact(contact)
    return customer

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
