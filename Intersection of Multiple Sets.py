question=Write a function that takes a list of sets and returns a set that is the intersection of all the sets in the list.
 
def intersection_of(sets):
    if not sets:
        return sets()
    result=sets[0]
    for s in sets[1::]:
        result = result.intersection(s)
    return result
sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
print(intersection_of(sets))
