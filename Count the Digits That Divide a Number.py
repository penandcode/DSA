# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        
        for digit in str(num):
            if num % int(digit) == 0:
                count += 1
                
        return count
        
