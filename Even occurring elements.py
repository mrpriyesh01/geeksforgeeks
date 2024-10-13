Given an array arr[] of integers, where most numbers occur an odd number of times, except for a few elements that appear an even number of times. 
Find and return the elements with even occurrences in the array.
If no such element exists, return -1.
Note: Elements should be returned in order of occurrence.

Input: arr[] = [9, 12, 23, 10, 12, 12, 15, 23, 14, 12, 15]
Output: [12, 15, 23]
Explanation: The numbers 12, 15, and 23 each appear an even number of times.
Input: arr[] = [23, 12, 56, 34, 32]
Output: [-1]
Explanation: Every number in the array occurs an odd number of times.



code=
class Solution:
    def findEvenOccurrences(self, arr):
        # code 
        d={}
        c=[]
        s=set()
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in arr:
            if d[i] % 2==0 and i not in s:
                c.append(i)
                s.add(i)
        if c:
            return c
        else:
            return [-1]

