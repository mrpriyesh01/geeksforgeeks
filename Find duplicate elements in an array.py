question=https://www.geeksforgeeks.org/find-duplicates-given-array-elements-not-limited-range/




class Solution:
    def findDuplicates(self, arr):
        # Sort the array first so duplicates are adjacent
        arr.sort()
        result = []  # List to store duplicates

        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:  # Check if the current element is the same as the previous
                if arr[i] not in result:  # Add to result only if it's not already there
                    result.append(arr[i])  # Append the duplicate element

        return result  # Return the list of duplicates

# Example usage:
solution = Solution()
arr = [2, 10, 10, 100, 2, 10, 11, 2, 11, 2]
duplicates = solution.findDuplicates(arr)
print(duplicates)  # Output: [2, 10, 11]
