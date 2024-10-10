Given an array arr[] with repeated elements, the task is to find the maximum distance between two occurrences of an element.

Note: You may assume that every input array has repetitions.

Examples:

Input: arr = [1, 1, 2, 2, 2, 1]
Output: 5
Explanation: distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, So max distance is 5.
Input: arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Output: 10

Code=
class Solution:
    # Function should return an integer
    def maxDistance(self, arr):
        # Dictionary to store the first occurrence index of each element
        first_occurrence = {}
        # Initialize a variable to track the maximum distance
        max_distance = 0
        # Iterate through the array
        for i, num in enumerate(arr):
            if num in first_occurrence:
                # Calculate the distance between the current index and the first occurrence
                distance = i - first_occurrence[num]
                # Update max_distance if this distance is larger
                max_distance = max(max_distance, distance)
            else:
                # If it's the first occurrence, store the index
                first_occurrence[num] = i
        
        # Return the maximum distance found
        return max_distance


        
        # Code here
