import unittest
from ex19_11 import enumOperator


class TestName(unittest.TestCase):

    def setUp(self):
        self.e = enumOperator()

    def test_read_name_file(self):
        d = self.e.read_name_file()
        self.assertEqual(d, "name\nstate_a\nstate_b\nstate_c\nstate_d\nstate_e\nstate_f\n")
