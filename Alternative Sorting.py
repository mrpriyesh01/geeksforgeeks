Given an array arr of distinct integers. Rearrange the array in such a way that the first element is the largest and the second element is the smallest, 
the third element is the second largest and the fourth element is the second smallest, and so on.

Examples:

Input: arr[] = [7, 1, 2, 3, 4, 5, 6]
Output: [7, 1, 6, 2, 5, 3, 4]
Explanation: The first element is first maximum and second element is first minimum and so on.
Input: arr[] = [1, 6, 9, 4, 3, 7, 8, 2]
Output: [9, 1, 8, 2, 7, 3, 6, 4]
Explanation: The first element is first maximum and second element is first minimum and so on.

code=
class Solution:
    def alternateSort(self, arr):
        arr.sort()
        left = 0
        right = len(arr) - 1
        result = []
        
        while left <= right:
            if left == right:
                result.append(arr[left])  # For the middle element in odd-length arrays
            else:
                result.append(arr[right])  # Append largest available element
                result.append(arr[left])   # Append smallest available element
            
            left += 1
            right -= 1
        
        return result


