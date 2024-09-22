Given an array arr, return the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

Examples:

Input: arr = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr = [10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist so answer is -1.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)


code=
class Solution:
    def print2largest(self, arr):
        n = len(arr)
        if n < 2:
            return -1  # Not enough elements for second largest

        # Initialize largest and second largest
        largest = arr[0]
        second_largest = -1

        for i in range(1, n):
            if arr[i] > largest:
                # Update second_largest before updating largest
                second_largest = largest
                largest = arr[i]
            elif arr[i] > second_largest and arr[i] != largest:
                # Update second_largest if current element is between largest and second largest
                second_largest = arr[i]

        return second_largest
