You are given two long numbers N1 and N2 in a string. You need to find out if the product of these numbers generate an even number or an odd number,
If it is an even number print 1 else print 0.

Example 1:

Input: 
N1 = "12"
N2 = "15"
Output: 1
Explanation: 12 * 15 = 180 which is an 
even number.
code=
#User function Template for python3
class Solution:
    def EvenOdd(self, n1, n2):
        n3 = n1 * n2
        if n3 % 2 == 0:
            return 1
        else:
            return 0
