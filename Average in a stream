Given a stream of incoming numbers, find average or mean of the stream at every point.
Example 1:
Input:
n = 5
arr[] = {10, 20, 30, 40, 50}
Output: 10.00 15.00 20.00 25.00 30.00 
Explanation: 
10 / 1 = 10.00
(10 + 20) / 2 = 15.00
(10 + 20 + 30) / 3 = 20.00
And so on.

code=
class Solution:
	def streamAvg(self, arr, n):
	    total_sum = 0
      result = []   
        for i in range(n):
            total_sum += arr[i]
            avg = total_sum / (i + 1)
            result.append(avg)
        return result
	
