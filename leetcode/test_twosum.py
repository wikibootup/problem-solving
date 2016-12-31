from twosum import Solution

import unittest


class TestTwoSum(unittest.TestCase):
    
    def setUp(self):
        self.ts = Solution()

    def test_small(self):
        small = list(range(20))
        target = 17 + 19
        self.assertListEqual([17, 19], self.ts.twoSum(small, target))

    def test_no_exist(self):
        small = list(range(5))
        target = 17 + 19
        self.assertListEqual([], self.ts.twoSum(small, target))

    @unittest.skip('too big')
    def test_big(self):
        small = list(range(200000))
        target = 179999 + 199999
        self.assertListEqual([179999, 199999], self.ts.twoSum(small, target))
