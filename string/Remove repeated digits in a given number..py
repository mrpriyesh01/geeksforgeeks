Given an integer N represented in the form of a string, remove consecutive repeated digits from it.

Example 1:

Input:
N = 1224
Output: 124
Explanation: Two consecutive occurrences of 
2 have been reduced to one.


Code=
# User function Template for python3

class Solution:
    def modify(self, N) -> str:
        N = str(N)
        if not N: 
            return ''
        result = N[0]  
        for i in range(1, len(N)):
            if N[i] != N[i - 1]:  
                result += N[i]  
        return result
      
      #second method
class Solution:
    def modify(self, N) -> str:
        N = str(N)  
        unique = "" 
        for i in range(len(N)): 
            if i == 0 or N[i] != N[i - 1]:  
                unique += N[i] 
        
        return unique  


