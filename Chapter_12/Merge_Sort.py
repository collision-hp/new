def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    leftsort=mergesort(left)
    rightsort=mergesort(right)
    return merge(leftsort,rightsort)
def merge(lefthalf,righthalf):
    final=[]
    i,j=0,0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i]<righthalf[j]:
            final.append(lefthalf[i])
            i+=1
        else:
            final.append(righthalf[j])
            j+=1
    final.extend(lefthalf[i:])
    final.extend(righthalf[j:])
    return final
arr=[12,42,56,1,386,31,23]
sorted=mergesort(arr)
print(sorted)