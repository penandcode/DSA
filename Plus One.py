# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = int("".join(map(str, digits)))
        number = number + 1
        return [int(x) for x in str(number)]
