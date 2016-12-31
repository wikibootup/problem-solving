# O(N^2)
# it is hard to pass the test big cases
class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sizeOfNums = len(nums)
        for i in range(sizeOfNums):
            for j in range(i+1, sizeOfNums):
                if target == nums[i] + nums[j]:
                    return [i, j]
        return []

'''
# O(N) by https://github.com/kamyu104/LeetCode/blob/master/Python/two-sum.py
class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []
'''
