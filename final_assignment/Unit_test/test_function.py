import unittest
from final_assignment.Front_app.Design import *
from final_assignment.set_get.retrive import *
from final_assignment.database_app.data import *


class Test_function1(unittest.TestCase):
    def setUp(self):
        self.second = Database()

    def test_delete(self):
        query = 'delete from customer where cus_Id=%s'
        value = (40,)
        self.second.delete(query, value)
        values = (40, 'Shikhar', 'Manandar',
                  'Bhaktapur', '980881111', 'Bhaktapur',
                  23, 'shikhar.com')
        query1 = "select * from customer where cus_Id=%s"
        expect = self.second.selectvalue(query1, value)
        self.assertNotIn([values], expect)

    def tearDown(self):
        self.second = None


class Test_functions2(unittest.TestCase):
    def setUp(self):
        self.first = Database()

    def test_add(self):
        query = 'insert into customer values (%s,%s,%s,%s,%s,%s,%s,%s)'
        values = (40, 'Shikhar', 'Manandar',
                  'Bhaktapur', '980881111', 'Bhaktapur',
                  23, 'shikhar.com')
        self.first.add(query, values)
        query1 = "select * from customer where cus_Id=%s"
        value1 = (40,)
        expect = self.first.selectvalue(query1, value1)
        self.assertEqual([values], expect)

    def tearDown(self):
        self.first = None


class Test_function3(unittest.TestCase):
    def setUp(self):
        self.third = Database()

    def test_update(self):
        query = 'update customer set first_name=%s where cus_Id=%s'
        value = ('Jofree', 40)
        aspected = [('Jofree',)]
        self.third.update(query, value)
        values = (40,)
        query1 = "select * from customer where cus_Id=%s"
        expect = self.third.selectvalue(query1, values)
        self.assertNotIn(aspected, expect)

    def tearDown(self):
        self.third = None


class Test_function4(unittest.TestCase):
    def setUp(self):
        self.a = Database()

    def test_selectvalue(self):
        query = 'select first_name from customer where cus_Id=%s'
        value = (1,)
        actual = self.a.selectvalue(query,value)
        expected = ('Anil',)

        self.assertEqual([expected],actual)

    def tearDown(self):
        self.a = None


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


class Test_Search(unittest.TestCase):
    def setUp(self):
        self.co = CustomerTable

    def test_search(self):
        list = [(1, 55, 89, 'bad', 5, 2), (3, 4, 5, 'good', 6, 7, 0), (53, 666, 77, 'average', 99, 100)]
        item = 'good'
        index = 3
        actual = self.co.search(item, list, index)
        self.assertEqual([list[1]], actual)

    def tearDown(self):
        self.co = None


class test_sort(unittest.TestCase):
    def setUp(self):
        self.so = CustomerTable

    def test_sort(self):
        list = [(1, 55, 89, 'bad', 5, 2), (3, 4, 5, 'good', 6, 7, 0), (53, 666, 77, 'average', 99, 100)]
        expected = [(3, 4, 5, 'good', 6, 7, 0), (1, 55, 89, 'bad', 5, 2), (53, 666, 77, 'average', 99, 100)]
        index = 1
        actual = self.so.sort(list, index)
        self.assertEqual(expected, actual)

    def tearDown(self):
        self.so = None


class test_clear(unittest.TestCase):
    def setUp(self):
        Tk()
        self.cl = CustomerDetails
        self.variable = StringVar()
        self.variable.set('jin')

    def test_solution(self):
        self.cl.solution([self.variable])
        self.assertEqual('', self.variable.get())

    def tearDown(self):
        self.variable = None


if __name__ == "__main__":
    unittest.main()
