Given a string s without spaces, the task is to remove all duplicate characters from it, keeping only the first occurrence.

Note: The original order of characters must be kept the same. 

Examples :
Input: s = "zvvo"
Output: "zvo"
Explanation: Only keep the first occurrence
Input: s = "gfg"
Output: "gf"
Explanation: Only keep the first occurrence
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Code=
class Solution:
    def removeDups(self, s):
        # Yeh array banate hain jo 256 characters ke liye hoga
        # ASCII characters ko store karne ke liye
        seen = [False] * 256
        result = []
        
        for char in s:
            # Agar character pehli baar mil raha hai
            if not seen[ord(char)]:  
                seen[ord(char)] = True  # Character ko mark kar do
                result.append(char)      # Character ko result mein daal do
        
        return ''.join(result)  # Result list ko string mein convert karke return karo

#secode mthod=
#User function Template for python3
class Solution:
    def removeDups(self, str):
        seen = set()         # Yeh set un characters ko track karega jo hum dekh chuke hain
        result = []          # Yeh list woh characters store karegi jo hum rakhna chahte hain

        for char in str:
            if char not in seen:  # Agar character pehli baar mil raha hai
                seen.add(char)     # Us character ko seen set mein daal do
                result.append(char) # Us character ko result mein daal do

        return ''.join(result)     # Result list ko string mein convert karke return karo

        
        # code here

