# Given an array of integers nums and an integer target, return indices of the two numbers 
# such that they add up to target.
#  You may assume that each input would have exactly one solution, and you may not use the same 
# element twice.
# You can return the answer in any order.

num=[1,2,3,4,5]
target=3

for i in range(len(num)):
    for j in range (i+1, len(num)):
        if (num[i]+num[j]==target):
            result1=i
            result2=j
            print(f"The indices are: ", result1 ,result2)
            break

