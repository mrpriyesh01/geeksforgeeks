Given an array arr of size n which contains elements in range from 0 to n-1, you need to find all the elements occurring more than once in the given array.
Return the answer in ascending order. If no such element is found, return list containing [-1]. 

Examples:
Input: n = 4, arr[] = [0,3,1,2]
Output: -1
Explanation: There is no repeating element in the array. Therefore output is -1.
Input: n = 5, arr[] = [2,3,1,2,3]
Output: 2 3 
Explanation: 2 and 3 occur more than once in the given array.

Brief Explanation
Initialize Sets:
seen: to track elements we've encountered.
dupli: to store duplicates.

Process List:
Iterate through each number. If it's already in seen, add to dupli. Otherwise, add it to seen.

Return Result:
Return [-1] if no duplicates. Otherwise, return sorted list of duplicates.

code=
from typing import List

class Solution:
    def duplicates(self, n: int, arr: List[int]) -> List[int]:
        seen = set()       # Track seen elements
        dupli = set()      # Store duplicates  
        for num in arr:
            if num in seen:
                dupli.add(num)  # Found a duplicate
            else:
                seen.add(num)   # First time seeing this number
        if not dupli:
            return [-1]       # No duplicates found
        return sorted(dupli)  # Return sorted list of duplicates


