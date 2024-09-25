Find first repeated character
Difficulty: EasyAccuracy: 41.97%Submissions: 83K+Points: 2
Given a string S. The task is to find the first repeated character in it. We need to find the character that occurs more than once and whose index of second occurrence is smallest. S contains only lowercase letters.
Example 1:
Input: S="geeksforgeeks"
Output: e
Explanation: 'e' repeats at third position.

Example 2:
Input: S="hellogeeks"
Output: l
Explanation: 'l' repeats at fourth position.

code=
class Solution:
    def firstRepChar(self, s):
        seen=set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)
        return -1
        # code here
