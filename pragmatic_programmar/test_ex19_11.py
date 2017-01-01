import unittest
from ex19_11 import enumOperator


class TestName(unittest.TestCase):

    def setUp(self):
        self.e = enumOperator()

    def test_read_name_file(self):
        d = self.e.read_name_file()
        self.assertEqual(d, "name\nstate_a\nstate_b\nstate_c\nstate_d\nstate_e\nstate_f\n")

    @unittest.skip('needed correct test text')
    def test_generate_c_file_from_name_file(self):
        self.e.gen_c_file()
        d = self.e.read_c_file('name.c')
        self.assertEqual(d, "extern const char*f NAME_names[];\ntypedef enum {\n\tstate_a,\n\tstate_b,\n\tstate_c,\n\tstate_d\n\tstate_e\n\tstate_f\n} NAME;\n")
