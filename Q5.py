import random
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]>=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quicksort(arr,low,high,k):
    if low<=high:
        pi=partition(arr,low,high)
        if pi==k:
            return arr[pi]
        elif pi<k:
            return quicksort(arr,pi+1,high,k)
        else:
            return quicksort(arr,low,pi-1,k)
    return None
def kth_largest(arr,k):
    n=len(arr)
    if k<1 or k>n:
        return None
    return quicksort(arr,0,n-1,k-1)

arr=[2,4,1,3,7,5]
k=3
print(f'The {k}th largest number in the array is {kth_largest(arr,k)}')

