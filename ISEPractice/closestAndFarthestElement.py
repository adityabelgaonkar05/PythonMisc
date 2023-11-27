list1 = eval(input())
diff = []
k = float(input())

for i in list1:
  diff.append(abs(i-k))

print("closest: " + str(list1[diff.index(min(diff))]))
print("farthest: " + str(list1[diff.index(max(diff))]))