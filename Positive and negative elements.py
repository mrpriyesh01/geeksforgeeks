Given an array arr containing equal number of positive and negative elements, arrange the array such that every positive element is followed by a negative element.
Note: The relative order of positive and negative numbers should be maintained.

Input: arr[] = [-1, 2, -3, 4, -5, 6]
Output: [2, -1, 4, -3, 6, -5]
Explanation: Positive numbers in order are 2, 4 and 6. Negative numbers in order are -1, -3 and -5. So the arrangement we get is 2, -1, 4, -3, 6 and -5.
Input: arr[] = [-3, 2, -4, 1]
Output: [2, -3, 1, -4] 
Explanation: The positive numbers are 2,1 and negetive numbers are -3, -4 

code=
class Solution:
    def arranged(self, arr):
        for i in range(0, len(arr), 2):
            if i + 1 < len(arr):  
                arr[i], arr[i+1] = arr[i+1], arr[i]
        return arr 

