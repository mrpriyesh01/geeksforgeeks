#Write a Python program to find all the anagrams and group them together from a given list of strings.Use the Python data type.


mystring = ["prem", "repm", "cat", "tac"]
anagrams = {}
for word in mystring:
    sorted_word = ''.join(sorted(word)) 
    if sorted_word not in anagrams:
        anagrams[sorted_word] = []
    anagrams[sorted_word].append(word)
print(list(anagrams.values()))
