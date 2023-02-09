# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for i in range(len(operations)):
            if(operations[i] == "X++" or operations[i] == "++X"):
                x = x + 1
            if(operations[i] == "X--" or operations[i] == "--X"):
                x = x - 1
        return x
