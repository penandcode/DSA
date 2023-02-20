# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = []
        sum = 0
        pro = 1
        while(n > 0):
            arr.append(n % 10)
            n = n // 10
        for i in range(len(arr)):
            sum += arr[i]
        for i in range(len(arr)):
            pro *= arr[i]
        return pro - sum
