Given an array, arr of n integers, and an integer element x, find whether element x is present in the array.
Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

Examples:
Input: arr[] = [1, 2, 3, 4], x = 3
Output: 2
code=
class Solution:
   
    def search(self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i  # Return the index of the element if found
        return -1  # Return -1 if the element is not found
