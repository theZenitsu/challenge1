from functools import reduce

List = [2, 4, 6, 9, 10]

mulitiplication_cumulatif = reduce(lambda x, y: x*y, List)
print("new list multiplication: ", mulitiplication_cumulatif)

