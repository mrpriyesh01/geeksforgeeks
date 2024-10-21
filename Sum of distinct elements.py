You are given an array arr. Find the sum of distinct elements in an array.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: 15
Explanation: Distinct elements are 1, 2, 3, 4, 5. So sum is 15.


explanation=
Steps:
=Use unique_set to store numbers we've seen for the first time.
=Use duplicate_set to track numbers that appear more than once.
=total_sum stores the sum of unique numbers.

How it works:
=For each number in arr:
=If it's not in unique_set, add it to the set and to total_sum.
=If it's a duplicate, add it to duplicate_set (no change to the sum).

code=
class Solution:
    def findSum(self, arr):
        unique_set = set()  # Set to track unique elements
        duplicate_set = set()  # Set to track duplicate elements
        total_sum = 0
        for num in arr:
            if num not in unique_set:
                # If it's not a duplicate, add to unique_set and total_sum
                unique_set.add(num)
                total_sum += num
            elif num not in duplicate_set:
                # If it's already in unique_set and not in duplicate_set, it's a duplicate
                duplicate_set.add(num)
        return total_sum
