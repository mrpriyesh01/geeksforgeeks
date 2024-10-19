Given string s that is appended with a number at last. The task is to check whether the length of string 
excluding that number is equal to that number.
Example 1:
Input:  s = "geeks5"
Output: 1
Explanation: Length of geeks is 5
and the last number is also 5.
  
Example 2:
Input:  s = "geek5"
Output: 0
Explanation: Length of geek is 4
and the last number is 5.

class Solution:
    def isSame(self, s):
        DIGIT = []

        # Traverse the string from the end to collect digits
        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():  # Check if the character is a digit
                DIGIT.append(s[i])  # Add the digit to the DIGIT list
            else:
                break  # Stop when we encounter a non-digit character

        # If no digits were found, return 0
        if not DIGIT:
            return 0

        # Reverse and join the digits to form the number
        number = int(''.join(reversed(DIGIT)))

        # Compare the length of the string excluding the digits
        if len(s) - len(DIGIT) == number:
            return 1
        else:
            return 0

# Example usage
solution = Solution()
s = "geeks5"
print(solution.isSame(s))  # Output: 1
