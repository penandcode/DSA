# https://leetcode.com/problems/is-subsequence/description/
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s: 
            return True
        matched = 0
        for l in t:
            if s[matched]==l:
                matched += 1
            if matched==len(s): 
                return True
        return False
