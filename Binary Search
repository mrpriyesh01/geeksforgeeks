Given a sorted array arr and an integer k, find the position(0-based indexing) at which k is present in the array using binary search.

Examples:

Input: k = 4, arr= [1, 2, 3, 4, 5]  
Output: 3
Explanation: 4 appears at index 3.

code=
#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==k:
                return mid
            elif arr[mid]<k:
                low=mid+1
            else:
                high=mid-1
        return -1 
