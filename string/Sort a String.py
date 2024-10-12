Given a string consisting of lowercase letters, arrange all its letters in ascending order. 

Example 1:

Input:
S = "edcab"
Output: "abcde"
Explanation: characters are in ascending
order in "abcde".
Example 2:

Input:
S = "xzy"
Output: "xyz"
Explanation: characters are in ascending
order in "xyz".

code=
#User function Template for python3
class Solution:
    def sort(self, s):
        convert=list(s) #convert string to list becouse string is unchangable that's why i using list
        convert.sort()  #sort the list
        return''.join(convert) #now back to string
        #code here
