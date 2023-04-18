#Time complexity is O(k) where k is half of the no of elements in the array
#Auxillary space O(1) since we are not using any extra space other than what is in the list

def rotate (New):
    n = len(New)
    k = int(n/2)
    j = n
    for i in range(k):
        New[j-1],New[i] = New[i],New[j-1]
        j -= 1
    return New

print("Hello world")
arr = [1,2,3,4,5,6,7,8,9,10]
globe = list(arr)
globeNew = rotate(globe)
print (globeNew)