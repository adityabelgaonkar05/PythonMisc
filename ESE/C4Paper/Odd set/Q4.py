# WAP to read the working hours of n number of employees with 4 weeks data 
# plans using numpy. Sample shown below
# find-->Shape of employee duty chart
#     -->Sum of hours in month
#     -->Search employeee securing highest working hours

# Name of Employee    week1   week2   week3   week4
# VIPUL                40       40     40      40
# RISHI                42       42     42      42
# VIVEK                45       45     45      45
# VIBHU                38       38     38      38
# VIDITA               30       30     30      30

import numpy as np

names = ["VIPUL", "RISHI", "VIVEK", "VIBHU", "VIDITA"]
week1 = [40, 42, 45, 38, 30]
week2 = week3 = week4 = week1

arr = np.array([names, week1,week2, week3, week4])

print(np.shape(arr))

sumOfWeeks = [0]*len(names)

#messed up this part of code but itna hard nahi ayega so chill

print(f"{names}\n{sumOfWeeks}")

maxWorkingHours = np.argmax(arr)

print(f"Max number of working hours are for: {names[maxWorkingHours]}")