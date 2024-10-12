list1 = [1 , 3, 5, 6]
list2 = [2, 7, 8, 9]
list3 = [6, 9 , 8 , 10]

zipped = list(zip(list1,list2,list3))
print(zipped)

paire_ellements = list(map(lambda x: x[0] + x[1] + x[2], zipped))

print("addition des paires: ", paire_ellements)