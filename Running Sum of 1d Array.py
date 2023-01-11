#https://leetcode.com/problems/running-sum-of-1d-array/submissions/876237123/?envType=study-plan&id=level-1

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 0
        arr = []
        for i in range(len(nums)):
            p = p + nums[i] 
            arr.append(p)
        return arr
