Given a string S, the task is to change the complete string to Uppercase or Lowercase depending upon the case for the first character.

Example 1:

Input:
S = "abCD"
Output: abcd
Explanation: The first letter (a) is 
lowercase. Hence, the complete string
is made lowercase.

Example 2:
Input: 
S = "Abcd"
Output: ABCD
Explanation: The first letter (A) is
uppercase. Hence, the complete string
is made uppercase.

  
  code=
class Solution:
    def modify(self, s):
        for char in s:
            if char.islower():
                return s.lower()
            else:
                return s.upper()
        # code here
