Input:
a1[] = {11, 7, 1, 13, 21, 3, 7, 3}
a2[] = {11, 3, 7, 1, 7}
Output:
Yes
Explanation:
a2[] is a subset of a1[]


code=
def isSubset( a1, a2, n, m):
    for a in a2:
        if a1.count(a) >= a2.count(a):
            continue
        else:
            return "No"
    return "Yes"
    
