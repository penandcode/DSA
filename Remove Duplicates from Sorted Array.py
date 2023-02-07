# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=1
        for s in range(1,len(nums)):
            if nums[s]!=nums[s-1]:
				nums[l]=nums[s]
				l += 1
        return l
