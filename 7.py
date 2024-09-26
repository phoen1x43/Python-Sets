text1 = "The quick brown fox jumps over the lazy dog"
list1 = text1.split()
text2 = "The slow turtle jumps under the energetic dog"
list2 = text2.split()
set1 = set(list1)
set2 = set(list2)
print(set1.intersection(set2))
