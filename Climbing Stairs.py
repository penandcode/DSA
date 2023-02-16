# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climb(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return climb(n-1) + climb(n-2)
        return climb(n)
    
    class Solution(object):
        def climbStairs(self, n):
            """
            :type n: int
            :rtype: int
            """
            a, b = 0, 1
            for i in range(1, n+1):
                a, b = b, b+a
            return b
