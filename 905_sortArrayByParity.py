class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        evens = [x for x in A if x%2 == 0 ]
        odds = [x for x in A if x%2 == 1]
        
        return evens + odds