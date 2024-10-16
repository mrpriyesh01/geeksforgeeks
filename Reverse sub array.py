Given an array arr, you need to reverse a subarray of that array. The range of this subarray is given by indices L and R (1-based indexing).

Examples:

Input: arr[] = [1, 2, 3, 4, 5, 6, 7] and L = 2 and R = 4
Output: [1, 4, 3, 2, 5, 6, 7]
Explanation: After reversing the elements in range 2 to 4 (2, 3, 4), modified array is 1, 4, 3, 2, 5, 6, 7.

Code=
#User function Template for python3

class Solution:
    def reverseSubArray(self, arr, l, r):
        # Reverse the subarray from index l to r
        l=l-1
        r=r-1
        arr[l:r+1] = arr[l:r+1][::-1]
        return arr
