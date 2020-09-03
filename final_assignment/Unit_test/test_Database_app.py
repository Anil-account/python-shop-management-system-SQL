import unittest
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
        actual = self.a.selectvalue(query, value)
        expected = ('Anil',)

        self.assertEqual([expected], actual)

    def tearDown(self):
        self.a = None


if __name__ == "__main__":
    unittest.main()
