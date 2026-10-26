# // Given an array arr[] of n integers and a target value, check if there exists a 
# // pair whose sum equals the target.

def twosum(arr, target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]+arr[j]==target:
                return True

    return False

if __name__=="__main__":
    arr=[1,2,3,4,5]
    target=3
    if twosum(arr, target):
        print("True")
    else:
        print("False")