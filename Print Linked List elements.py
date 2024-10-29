Given a linked list. Print all the elements of the linked list separated by space followed.

Examples:

Input: LinkedList : 1 -> 2

Output: 1 2
Explanation: The linked list contains two elements 1 and 2.The elements are printed in a single line.

code=
#Your function should print the data in one line only

'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    # Function to display the elements of a linked list
    def display(self, head):
        current = head
        # Traverse the linked list until the end
        while current:
            print(current.data, end=" ")
            current = current.next
