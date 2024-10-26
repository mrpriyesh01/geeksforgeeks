Given a string, your task is to reverse the string keeping the spaces intact to their positions.

Example 1:

Input:
S = "Help others"
Output: sreh topleH
Explanation: The space is intact at index 4
while all other characters are reversed.
Example 2:

Input: 
S = "geeksforgeeks"
Output: skeegrofskeeg
Explanation: No space present, hence the
entire string is reversed.


code=

class Solution:
    def reverseWithSpacesIntact(self, s):
        chars = list(s)  
        left, right = 0, len(s) - 1  
        
        while left < right:
            if chars[left] == ' ':  
                left += 1
            elif chars[right] == ' ':  
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1  
                right -= 1 
        
        return ''.join(chars)  

