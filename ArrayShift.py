#Time complexity O(n) where n is the number of shifts provided by the user
#Space complexity = O(1) since we are using only 1 temp variable and overwriting
#on top of it everytime the function is called

def shift (n, New):
    
    for i in range(0,n):
        temp = New.pop(0)
        New.append(temp)
    return New

print("Hello world")
arr = [1,2,3,4,5,6,7,8,9,10]
globe = list(arr)
ShiftNum = int(input())
globeNew = shift(ShiftNum, globe)
print (globeNew)