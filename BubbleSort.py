# Bubble sort using python
# This code has the worst case complexity as O(n*n), that is when the list is in the reverse order
#This code has the best case complexity as O(n) as it traverse the list once with the inner loop,
 #if nothing is swapped then it will exit the code and doesn't traverse the list once again.

def bubbleSort(myList):
    for i in range(len(myList)-1):
        swapped = False
        for j in range(len(myList)-1-i):
            if myList[j]>myList[j+1]:
                myList[j],myList[j+1]=myList[j+1],myList[j]
                swapped=True
        if swapped == False:
                break
    return myList

print bubbleSort([4,1,3])
print bubbleSort([2,3,1,4,5,3])
print bubbleSort([1,1,1,4,5,3])

# if you want the sorted unique list then apply the set() to the returned list.