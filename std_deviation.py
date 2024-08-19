import math
def stddeviation(arr):
    N=len(arr)
    avg=0
    for i in range(N):
        avg=avg+arr[i]
    avg=avg/N

    sum=0
    for i in arr:
        sum=sum+((i-avg)**2)
    sum=sum/N
    return math.sqrt(sum)
print(stddeviation([1,2,3]))
