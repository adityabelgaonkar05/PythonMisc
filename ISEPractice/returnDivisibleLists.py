test_list = eval(input())
k = int(input())

list2 = list(filter(lambda a : a[0]%k == 0 and a[1]%k == 0, test_list))

print(list2)