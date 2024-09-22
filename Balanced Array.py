Given an array arr of even size, the task is to find a minimum value that can be added to an element 
so that the array becomes balanced. An array is balanced if the sum of the left half of the array elements is equal to the sum of the right half.

Examples :
Input: arr = [1, 5, 3, 2]
Output: 1
Explanation: Sum of first 2 elements is 1 + 5  = 6, Sum of last 2 elements is 3 + 2  = 5, To make the array balanced you can add 1.
Input: arr = [1, 2, 1, 2, 1, 3]
Output: 2
Explanation: Sum of first 3 elements is 1 + 2 + 1 = 4, Sum of last three elements is 2 + 1 + 3 = 6, To make the array balanced you can add 2.


code=
class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        # Initialize sums for the two halves
        sum_first_half = 0
        sum_second_half = 0
        
        # Calculate the sum of the first half
        for i in range(len(arr) // 2):
            sum_first_half += arr[i]
        
        # Calculate the sum of the second half
        for i in range(len(arr) // 2, len(arr)):
            sum_second_half += arr[i]
        
        # Return the absolute difference between the two sums
        return abs(sum_first_half - sum_second_half)
