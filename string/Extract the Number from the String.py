Given a sentence containing several words and numbers. Find the largest number among them which does not contain 9. If no such number exists, return -1.

Note: Numbers and words are separated by spaces only. It is guaranteed that there are no leading zeroes in the answer.

Examples :

Input: sentence="This is alpha 5057 and 97"
Output: 5057
Explanation: 5057 is the only number that does not have a 9.
Input: sentence="Another input 9007"
Output: -1
Explanation: Since there is no number that does not contain a 9,output is -1.



code=
class Solution:
    def ExtractNumber(self, sentence):
        # Split the sentence into words
        words = sentence.split()
        largest_num = -1  

       
        for word in words:
            if word.isdigit():
                if '9' not in word:
                    num = int(word)
                    if num > largest_num:
                        largest_num = num

        return largest_num  
