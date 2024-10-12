A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.


Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
code=
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to a list of characters
        char_list = list(s)
        # Convert all characters to lowercase
        char_list = [char.lower() for char in char_list]
        # Remove non-alphanumeric characters
        char_list = [char for char in char_list if char.isalnum()]
        # Reverse the list
        reversed_list = char_list[::-1]
