Given a positive integer n, determine whether it is odd or even. Return a string "even" if the number is even and "odd" if the number is odd.

Examples:

Input: n = 15
Output: odd
Explanation: The number is not divisible by 2

code=
class Solution:
    def oddEven (ob,n):
        if n%2==0:
            return "even"
        else:
            return "odd"
        # code here 
