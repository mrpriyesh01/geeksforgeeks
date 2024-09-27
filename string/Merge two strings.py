Given two strings S1 and S2 as input, the task is to merge them alternatively i.e. the first character of S1 then the first character of S2 and so on till the strings end.
NOTE: Add the whole string if other string is empty.

Example 1:

Input:
S1 = "Hello" S2 = "Bye"
Output: HBeylelo
Explanation: The characters of both the 
given strings are arranged alternatlively.
â€‹Example 2:

Input: 
S1 = "abc", S2 = "def"
Output: adbecf
Explanation: The characters of both the
given strings are arranged alternatlively.

Code=
class Solution:
    def merge(self, S1, S2):
        result = ""
        # Loop through both strings up to the length of the shorter one
        for i in range(min(len(S1), len(S2))):
            result += S1[i] + S2[i]
        
        # Add the remaining characters from the longer string
        if len(S1) > len(S2):
            result += S1[i+1:]
        else:
            result += S2[i+1:]
        
        return result
