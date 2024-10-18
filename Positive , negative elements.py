Given an array arr containing equal number of positive and negative elements, arrange the array such that every positive element is followed by a negative element.
Note: The relative order of positive and negative numbers should be maintained.

Examples:

Input: arr[] = [-1, 2, -3, 4, -5, 6]
Output: [2, -1, 4, -3, 6, -5]
Explanation: Positive numbers in order are 2, 4 and 6. Negative numbers in order are -1, -3 and -5. So the arrangement we get is 2, -1, 4, -3, 6 and -5.


Solution:
    def arranged(self, arr):
        pos = []  # List to store positive numbers
        neg = []  # List to store negative numbers

        # Separate the array into positive and negative numbers
        for num in arr:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        result = []  # Final arranged array

        # Now, merge them alternatively: one positive, one negative
        for i in range(len(pos)):  # Since there are equal positive and negative numbers
            result.append(pos[i])
            result.append(neg[i])

        return result
