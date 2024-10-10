Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.

If the characters in str1 can be changed to get str2, then two strings, str1 and str2, are isomorphic. 
A character must be completely swapped out for another character while maintaining the order of the characters. A character may map to itself, but no two characters may map to the same character.

Example 1:

Input:
str1 = aab
str2 = xxy
Output: 
1
Explanation: 
There are two different characters in aab and xxy, i.e a and b with frequency 2 and 1 respectively.

code=
#User function Template for python3

class Solution:
    
    # Function to check if two strings are isomorphic.
    def areIsomorphic(self, str1, str2):
        # Check if lengths are different
        if len(str1) != len(str2):
            return False
        
        mapping_char1 = {}  # Mapping from characters in str1 to str2
        mapping_char2 = {}  # Mapping from characters in str2 to str1
        
        for char1, char2 in zip(str1, str2):
            # Check if char1 is already mapped
            if char1 in mapping_char1:
                if mapping_char1[char1] != char2:
                    return False  # Inconsistent mapping
            else:
                mapping_char1[char1] = char2  # Create a new mapping

            # Check if char2 is already mapped
            if char2 in mapping_char2:
                if mapping_char2[char2] != char1:
                    return False  # Inconsistent mapping
            else:
                mapping_char2[char2] = char1  # Create a new mapping
        
        return True  # All mappings are consistent

                
                
