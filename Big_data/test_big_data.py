import unittest, timeit
from Big_data import big_data as b
from memory_profiler import profile


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.data_a_1 = 3
        self.data_b_1 = 4
        self.data_n_1 = (1, 1, 1)
        self.data_m_1 = (1, 1, 1, 1)
        self.sum_1 = 6000000006

        self.data_a_2 = 5
        self.data_b_2 = 3
        self.data_n_2 = (1, 2, 3, 4, 5)
        self.data_m_2 = (6, 7, 8)
        self.sum_2 = 25000000045

        self.data_a_3 = 7
        self.data_b_3 = 4
        self.data_n_3 = (0, 7, 1, 7, 6, 7, 6)
        self.data_m_3 = (4, 1, 9, 7)
        self.sum_3 = 55000000068

        self.big_a = 100000
        self.big_data = range(self.big_a)

    def test_find(self):
        self.assertEqual(b.find(self.data_a_1, self.data_b_1, self.data_n_1, self.data_m_1), self.sum_1)
        self.assertEqual(b.find(self.data_a_2, self.data_b_2, self.data_n_2, self.data_m_2), self.sum_2)
        self.assertEqual(b.find(self.data_a_3, self.data_b_3, self.data_n_3, self.data_m_3), self.sum_3)

    def test_time(self):
        print(timeit.timeit(stmt='b.read_file()', number=1, globals=globals()))
        print(timeit.timeit(stmt='b.begin()', number=1, globals=globals()))


    @profile
    def test_memory(self):
        b.begin()


if __name__ == '__main__':
    unittest.main()
