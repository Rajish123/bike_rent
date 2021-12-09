import unittest
from datetime import datetime, timedelta
from bikerent_class import BikeRent
from customer_class import Customer

class BikeRentalTest(unittest.TestCase):
    def testdisplay_correct_stock(self):
        shop1 = BikeRent(0,0,0)
        shop2 = BikeRent(10,10,10)
        self.assertEqual(shop1.display_info(), (0, 0, 0))
        self.assertEqual(shop2.display_info(), (10,10,10))

    def testHourlyBasis(self):
        shop = BikeRent(10,10,10)
        self.assertEqual(shop.HourlyBasis(1, -1), None)
        self.assertEqual(shop.HourlyBasis(1,20), None)
        self.assertEqual(shop.HourlyBasis(1,5).hour, datetime.now().hour)

    def testDailyBasis(self):
        shop = BikeRent(10,10,10)
        result1 = shop.DailyBasis(1,-1)
        result2 = shop.DailyBasis(1, 20)
        result3 = shop.DailyBasis(3, 5).hour
        self.assertEqual(result1, None)
        self.assertEqual(result2, None)
        self.assertEqual(result3, datetime.now().hour)

    def testWeeklyBasis(self):
        shop = BikeRent(10,10,10)
        result1 = shop.DailyBasis(1,-1)
        result2 = shop.DailyBasis(1, 20)
        result3 = shop.DailyBasis(2, 5).hour
        self.assertEqual(result1, None)
        self.assertEqual(result2, None)
        self.assertEqual(result3, datetime.now().hour)

    def testReturnBikeForInvalidRentalTime(self):
        shop = BikeRent(10, 10, 10)
        customer = Customer()
        # here customer hasnt rent any bike and tried to return one
        request = customer.return_bike()
        # assertIsNone() in Python is a unittest library function that is used in unit testing to check that input value is None or not. 
        self.assertIsNone(shop.CalculateCost(request))
        # manually check return function with error values
        self.assertIsNone(shop.CalculateCost((0,0,0,0)))

    def testReturnBikeForInvalidRentalBasis(self):
        # create a shop and costumer object
        shop = BikeRent(10,10,10)
        customer = Customer()
        # create a valid bike_type, num_of_bike, rentalTime
        customer.bike_type = 1
        customer.num_of_bike = 5
        customer.rentalTime = datetime.now()
        # create invalid rentalbasis
        customer.rentalBasis = 10
        request = customer.return_bike()
        self.assertEqual(shop.CalculateCost(request), None)

    def testReturnBikeForInvalidNumOfBike(self):
        shop = BikeRent(10,10,10)
        customer = Customer()
        # create a valid bike_type, rentalBasis rentalTime
        customer.bike_type = 1
        customer.rentalBasis = 1
        customer.rentalTIme = datetime.now()
        # create a invalid num of bike
        customer.num_of_bike = 0
        request = customer.return_bike()
        self.assertEqual(shop.CalculateCost(request), None)

    def testReturnBikeForValidCredentials(self):
        # create shop and various customers
        shop = BikeRent(50,50,50)
        customer1 = Customer()
        customer2 = Customer()
        customer3 = Customer()
        customer4 = Customer()
        customer5 = Customer()
        customer6 = Customer()

        # create valid bike model
        # royal_enfield
        customer1.bike_name = 1
        customer2.bike_name = 1
        # ktm
        customer3.bike_name = 2
        customer4.bike_name = 2
        # cf
        customer5.bike_name = 3
        customer6.bike_name = 3

        # create valid num_of bike
        customer1.num_of_bike = 1
        customer2.num_of_bike = 5
        customer3.num_of_bike = 2
        customer4.num_of_bike = 8
        customer5.num_of_bike = 15
        customer6.num_of_bike = 30

        # create valid rental basis for each customer
        # hourly basis
        customer1.rentalBasis = 1
        customer1.rentalBasis = 1
        # daily basis
        customer1.rentalBasis = 2
        customer1.rentalBasis = 2
        # weekly basis
        customer1.rentalBasis = 3
        customer1.rentalBasis = 3

        # create a valid rental time
        customer1.rentalTime = datetime.now() - timedelta(hours=-4)
        customer2.rentalTime = datetime.now() - timedelta(hours=-22)
        customer3.rentalTime = datetime.now() - timedelta(days=-4)
        customer4.rentalTime = datetime.now() - timedelta(days=-13)
        customer5.rentalTime = datetime.now() - timedelta(weeks=-6)
        customer6.rentalTime = datetime.now() - timedelta(weeks=-12)

        # make all customer return their bikes
        request1 = customer1.return_bike()
        request2 = customer2.return_bike()
        request3 = customer3.return_bike()
        request4 = customer4.return_bike()
        request5 = customer5.return_bike()
        request6 = customer6.return_bike()

        # check all of them get correct bill
        # self.assertEqual(shop.CalculateCost(request1), 1000)
        # self.assertEqual(shop.CalculateCost(request2), 402.5)
        # self.assertEqual(shop.CalculateCost(request3), 160)
        # self.assertEqual(shop.CalculateCost(request4), 2080)
        # self.assertEqual(shop.CalculateCost(request5), 5400)
        # self.assertEqual(shop.CalculateCost(request6), 21600)

class CustomerTest(unittest.TestCase):
    def testReturnBikeWithValidInput(self):
        customer = Customer()
        now = datetime.now()
        customer.bike_type = 1
        customer.rentalBasis = 1
        customer.rentalTime = now
        customer.num_of_bike = 10
        self.assertEqual(customer.return_bike(), (1,10,1,now))

    def testReturnBikeWithInvalidInput(self):
        customer = Customer()
        now = datetime.now()
        customer.bike_type = 0
        customer.rentalBasis = 0
        customer.rentalTime = now
        customer.num_of_bike = 10
        self.assertEqual(customer.return_bike(), (0,0,0,0))

if __name__ == "__main__":
    unittest.main()