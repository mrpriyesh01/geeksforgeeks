Given a string consisting of lowercase english alphabets, reverse only the vowels present in it and print the resulting string.

Example 1:

Input:
S = "geeksforgeeks"
Output: geeksforgeeks
Explanation: The vowels are: e, e, o, e, e
Reverse of these is also e, e, o, e, e.

Example 2:

Input: 
S = "practice"
Output: prectica
Explanation: The vowels are a, i, e
Reverse of these is e, i, a.

Code=
#User function Template for python3

class Solution:
    def modify(self, s):
        vowels='aeiou'
        vowels_collect=[]
        for char in s:
            if char in vowels:
                vowels_collect.append(char)
        vowels_collect.reverse()
        result=[]
        vowel_index=0
        for char in s:
            if char in vowels:
                result.append(vowels_collect[vowel_index])
                vowel_index +=1
            else:
                result.append(char)
        return''.join(result)
