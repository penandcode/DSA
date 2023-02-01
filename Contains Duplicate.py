# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        l = len(nums)
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                return True
        return False
