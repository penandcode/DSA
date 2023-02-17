# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max = len(sentences[0].split(" "))
        for i in range(len(sentences)):
            if(len(sentences[i].split(" "))>max):
                max = len(sentences[i].split(" "))
        return max
