Given an array of N distinct elements, the task is to find all elements in array except two greatest elements in sorted order.
Example 1:
Input : 
a[] = {2, 8, 7, 1, 5}
Output :
1 2 5 
Explanation :
The output three elements have two or
more greater elements.   


code=
class Solution:
    def findElements(self,a, n):
        a.sort()
        return a[:len(a)-2]
