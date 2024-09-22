Given a string S, the task is to create a string with the first letter of every word in the string.
 

Example 1:

Input: 
S = "geeks for geeks"
Output: gfg

Code=
class Solution:
    def firstAlphabet(self, S):
        result = ""
        for word in S.split():
            result += word[0]  # Collecting the first letter of each word
        return result
