def evennumber():
    list1 = []
    for i in range(4, 31):  
        if i % 2 == 0:
            list1.append(i)
    return list1
evennumber()
print(evennumber())

