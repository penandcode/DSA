# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        arr = []
        for i in range(len(candies)):
            if(candies[i] + extraCandies>= max(candies)):
                arr.append(True)
            else:
                arr.append(False)
        return arr
