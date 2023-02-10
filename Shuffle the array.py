# https://leetcode.com/problems/shuffle-the-array/

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        start = 0
        mid = n
        result = []

        while mid < 2*n:

            result.append(nums[start])
            result.append(nums[mid])
            start = start + 1
            mid = mid + 1

        return result
