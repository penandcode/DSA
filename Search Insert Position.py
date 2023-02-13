# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while right>=left:
            mid = (left + right)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
                
        return left
