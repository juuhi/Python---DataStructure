import sys
def mergeSort(A):
    merge_sort2(A,0,len(A)-1)

def merge_sort2(A,first,last):
    if first<last:
        middle = (first+last)/2
        merge_sort2(A,first,middle)
        merge_sort2(A,middle+1,last)
        merge(A,first,middle,last)

def merge(A,first,middle,last):
    L=A[first:middle+1]
    R=A[middle+1:last+1]
    L.append(999999)
    R.append(999999)
    i=j=0
    for k in range(first,last+1):
        if L[i]<=R[j]:
            A[k] = L[i]
            i =i+1
        else:
            A[k] = R[j]
            j=j+1

A = [5, 9, 1, 2, 4, 8, 6, 3, 7]
print(A)
mergeSort(A)
print(A)
B = [3,4,2]
mergeSort(B)
print(B)