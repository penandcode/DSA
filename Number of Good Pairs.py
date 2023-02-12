# https://leetcode.com/problems/number-of-good-pairs/

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i < j):
                    if(nums[i] == nums[j]):
                        n = n + 1
        
        return n
