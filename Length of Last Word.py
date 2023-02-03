# https://leetcode.com/problems/length-of-last-word/solutions/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])
