Given an unsorted array arr[] and two elements num1 and num2. 
The task is to count the number of elements that occur between the given elements (excluding num1 and num2).
If there are multiple occurrences of num1 and num2, we need to consider the leftmost occurrence of num1 and the rightmost occurrence of num2.

Examples:
class Solution:
    def getCount(self, arr, num1, num2):
        left_index = -1
        right_index = -1
        
        # Find leftmost occurrence of num1
        for i in range(len(arr)):
            if arr[i] == num1:
                left_index = i
                break
        # Find rightmost occurrence of num2
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == num2:
                right_index = i
                break
        
        # If num1 or num2 was not found, or if their order is incorrect
        if left_index == -1 or right_index == -1 or left_index >= right_index:
            return 0
        
        # Count elements between left_index and right_index
        return right_index - left_index - 1
