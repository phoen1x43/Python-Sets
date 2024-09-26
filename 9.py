s = []
letters = {'l', 'e', 't', 't', 'e', 'r', 's'}
words = ["rat", "star", "art", "set", "rest", "tea"]
for i in words:
 if set(i).difference(letters):
    pass
 else:
    s.append(i)
finalset = set(s)
print(finalset)
