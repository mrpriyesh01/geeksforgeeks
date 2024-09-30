Given a alphanumeric string S, extract maximum numeric value from S.

Example 1:
Input:
S = 100klh564abc365bg
Output: 564
Explanation: Maximum numeric value 
among 100, 564 and 365 is 564.
Example 2:

Input:
S = abcdefg
Output: -1
Explanation: Return -1 if no numeric 
value is present.
code=
#User function Template for python3
class Solution:
    def extractMaximum(self, S): 
        num = ""  # Temporary string to hold digits
        l = []    # List to store complete numbers
        
        # Loop through each character in the input string S
        for i in S:
            if i.isdigit():  # Check if the character is a digit
                num += i  # If it's a digit, add it to num
            else:
                if num != "":  # If we reach a non-digit and num is not empty
                    l.append(int(num))  # Convert num to an integer and add to the list
                    num = ""  # Reset num for the next number
        # If there are remaining digits in num after the loop, add them to the list
        if num != "":
            l.append(int(num))
        # If the list is empty, return -1
        if len(l) == 0:
            return -1
        # Return the maximum number found in the list
        return max(l)
