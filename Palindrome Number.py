# https://leetcode.com/problems/palindrome-number/solutions/
class Solution:
    def isPalindrome(self, x):
        a=str(x)
        b=a[::-1]
        if str(x)==b:
            return True
        else:
            return False
