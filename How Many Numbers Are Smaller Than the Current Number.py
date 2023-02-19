# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if(nums[i] > nums[j]):
                    count = count + 1
            arr.append(count)
        return arr
