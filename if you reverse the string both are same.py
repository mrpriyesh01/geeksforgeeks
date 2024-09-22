Given a string S, check if it is palindrome or not.

Example 1:
Input: S = "abba"
Output: 1
Explanation: S is a palindrome
Example 2:

Input: S = "abc" 
Output: 0
Explanation: S is not a palindrome

Code=
class Solution:
    def isPalindrome(self, S):
        left, right = 0, len(S) - 1
        while left < right:
            if S[left] != S[right]:
                return 0  # Return 0 if a mismatch is found
            left += 1
            right -= 1
        return 1  # Return 1 if the string is a palindrome
	    
	    
