import unittest
from final_assignment.set_get.retrive import *


class Test_Product1(unittest.TestCase):
    def setUp(self):
        self.fourth = ProductData('football Shoe', 1, 1, 10000, 20, 'Nike original shoe', 5)

    def test_set_name(self):
        self.fourth.set_name("Futsal shoe")
        self.assertEqual('Futsal shoe', self.fourth.get_name())

    def tearDown(self):
        self.fourth = None


class Test_Product2(unittest.TestCase):
    def setUp(self):
        self.fifth = ProductData('football Shoe', 1, 1, 10000, 20, 'Nike original shoe', 5)

    def test_get_name(self):
        self.assertEqual('football Shoe', self.fifth.get_name())

    def tearDown(self):
        self.fifth = None


class Test_Customer1(unittest.TestCase):
    def setUp(self):
        self.sixth = Customer(1, 'Bibek', 'Rai', 'Koteshwor', '90000', 'Koteshwor chok', 30, 'bibek.com')

    def test_set_id(self):
        self.sixth.set_first_name('Rina')
        self.assertEqual('Rina', self.sixth.get_first_name())

    def tearDown(self):
        self.sixth = None


class Test_Customer2(unittest.TestCase):
    def setUp(self):
        self.seventh = Customer(1, 'Bibek', 'Rai', 'Koteshwor', '90000', 'Koteshwor chok', 30, 'bibek.com')

    def test_get_id(self):
        self.assertEqual('Bibek', self.seventh.get_first_name())

    def tearDown(self):
        self.seventh = None


class Test_Offer1(unittest.TestCase):
    def setUp(self):
        self.o = Offer(1, 10, 1, 'gaming')

    def test_set_discount(self):
        self.o.set_discount(50)
        self.assertEqual(50, self.o.get_discount())

    def tearDown(self):
        self.o = None


class Test_Offer2(unittest.TestCase):
    def setUp(self):
        self.o = Offer(1, 10, 1, 'gaming')

    def test_get_discount(self):
        self.assertEqual(10, self.o.get_discount())

    def tearDown(self):
        self.o = None


class Test_Buy1(unittest.TestCase):
    def setUp(self):
        self.bu = Buy(1, '123@gmail.com', 2, 1, '2020-08-19')

    def test_set_email(self):
        self.bu.set_email('12@cloud.com')
        self.assertEqual('12@cloud.com', self.bu.get_mail())

    def tearDown(self):
        self.bu = None


class Test_Buy2(unittest.TestCase):
    def setUp(self):
        self.bu = Buy(1, '123@gmail.com', 2, 1, '2020-08-19')

    def test_get_mail(self):
        self.assertEqual('123@gmail.com', self.bu.get_mail())

    def tearDown(self):
        self.bu = None


if __name__ == "__main__":
    unittest.main()
