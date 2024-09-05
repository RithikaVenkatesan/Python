def findLargest(arr):
    largest=secLargest=0
    for i in range(len(arr)):
        if arr[i]>largest:
            secLargest=largest
            largest=arr[i]
        else:
            secLargest=max(secLargest,arr[i])
    return secLargest
print(findLargest([2,6,7,86,9,4]))
