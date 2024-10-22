Given a string s, extract all the integers from s.

Example 1:
Input:
s = "1: Prakhar Agrawal, 2: Manish Kumar Rai, 
     3: Rishabh Gupta56"
Output: 1 2 3 56
Explanation: 
1, 2, 3, 56 are the integers present in s.

code=
import re
class Solution:
    def extractIntegerWords(self, s):
        # Step 1: Use regex to find all sequences of digits in the string
        resut=[]
        result = re.findall(r'\d+', s)
        # Step 2: If there are any numbers, return them as a list
        if result:
            return result
        else:
            return []  # If no integers are found, return an empty list
      
