#WAP to read the numpy array, then find the maximum number in an 
#array, sort the entire array and finally search the specific number 
#by user choice

import numpy as np

arr = np.array(list(map(int, input().split())))

maxnum = max(arr)
print(f"{maxnum} is the maximum value")

arr.sort()
print(f"Sorted array is {arr}")

n = int(input("Enter number to search for: "))
if n in arr:
    print(f"{n} exists in array")

else: print(f"{n} does not exist in array")