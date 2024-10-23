Given a positive integer, N. Find the factorial of N.
 

Example 1:

Input:
N = 5
Output:
120
Explanation:
5*4*3*2*1 = 120
Example 2:

Input:
N = 4
Output:
24
Explanation:
4*3*2*1 = 24
code=

class Solution:
    def factorial(self, N):
      
        if N < 0:
            return "Factorial is not defined for negative numbers"
        
        result = 1
        for i in range(2, N + 1):
            result *= i
        return result
