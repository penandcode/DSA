# https://leetcode.com/problems/shuffle-string/

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        string = ""
        for i in range(len(indices)):
            string += s[indices.index(i)]
        return string
