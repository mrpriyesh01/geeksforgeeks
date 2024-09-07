Input: arr = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.

code=

class Solution:
    def rotate(self, arr):
        # Check if the array is empty or has only one element
        if len(arr) <= 1:
            return arr
        
        # Store the last element
        last_element = arr[-1]
        
        # Shift elements to the right by one position
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]
        
        # Place the last element at the first position
        arr[0] = last_element
        
        return arr

    

