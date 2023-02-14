# https://leetcode.com/problems/jewels-and-stones/

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = Counter(jewels)
        ans = 0
        for stone in stones:
            ans += count[stone]
        return ans   
