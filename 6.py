set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}
print(set1.intersection(set2, set3))
print(set1.difference(set2, set3))
print(set2.difference(set1, set3))
print(set3.difference(set1, set2))
