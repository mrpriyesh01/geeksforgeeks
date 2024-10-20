Given an odd number in the form of string, the task is to make largest even number possible from the given number
provided one is allowed to do exactly only one swap operation, if no such number is possible then return the input string itself.

Example 1:
Input:
s = 4543
Output: 4534
Explanation: Swap 4(3rd pos) and 3.
 

Example 2:
Input:
s = 1539
Output: 1539
Explanation: No even no. present.

code=
#User function Template for python3
class Solution:
    def makeEven(self, s):
        last_even_index = -1
        for i in range(len(s)):
            if int(s[i]) % 2 == 0:
                last_even_index = i
        if last_even_index == -1:
            return s
        s = list(s)  # Convert string to list for swapping
        for i in range(len(s)):
            if int(s[i]) % 2 == 0 and int(s[i]) < int(s[-1]):
                s[i], s[-1] = s[-1], s[i]  # Swap
                return ''.join(s) 
        # If no smaller even number is found, swap with the last even digit
        s[last_even_index], s[-1] = s[-1], s[last_even_index]
        return ''.join(s)

             
             
