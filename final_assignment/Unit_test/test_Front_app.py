import unittest
from final_assignment.Front_app.Design import *


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

