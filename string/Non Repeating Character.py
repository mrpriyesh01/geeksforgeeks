Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. 
If there is no non-repeating character, return '$'.

Note: When you return '$' driver code will output -1.
Examples:
Input: s = "hello"
Output: h
Explanation: In the given string, the first character which is non-repeating is h, as it appears first and there is no other 'h' in the string.
Input: s = "zxvczbtxyzvy"
Output: c
Explanation: In the given string, 'c' is the character which is non-repeating


code=
#User function Template for python3
class Solution:
    def nonrepeatingCharacter(self, s):
        # Step 1: Create an empty dictionary
        char_count = {}

        # Step 2: Count occurrences of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1  # Increment count if character is already in dictionary
            else:
                char_count[char] = 1  # Add character with count 1 if it's new

        # Step 3: Find the first non-repeating character
        for char in s:
            if char_count[char] == 1:  # Check if count is 1
                return char  # Return the first non-repeating character
        
        # If no non-repeating character is found, return '$'
        return '$'
