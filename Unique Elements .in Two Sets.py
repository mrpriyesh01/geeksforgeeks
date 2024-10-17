: Write a function that takes two sets and returns a set of elements that are unique to each set (i.e., elements that are in one set but not in the other).


code=
ef uniqueof(set1, set2):
    unique_items = []  
    for item in set1:
        if item not in set2:
            unique_items.append(item)  
            
    for item in set2:
        if item not in set1:
            unique_items.append(item)  
    return unique_items 

set1 = {2, 3, 4, 5, 6}
set2 = {2, 3, 11, 12, 13}
print(uniqueof(set1, set2))  
