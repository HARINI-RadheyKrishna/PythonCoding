#Not the optimized code
# Time complexity = 2 * O(d) where d is the number of digits in a number 
# Space complexity = O(d) where d is the number of digits in a number stored in an array here

def reversePy (num):
    i = 0
    d = 0
    arr1 = list()
    while num >= 10:
        d = int(num % 10)
        arr1.insert(i, d)
        i +=1
        num = num/10
        #print("Number",num)
    
    arr1.insert(i,int(num))
    #print (i+1)
    #print ("Array elements" ,arr1)
    #print(d)
    n = len(arr1)
    numNew = 0
    for j in range(0, n):
        k = arr1[j]
        numNew = (pow(10, n-1-j) * k) + numNew
        #print("NumNew", numNew)
    return numNew

print("Hello world")
Num = int(input())
Num = reversePy (Num)
print (Num)


#OPTIMIAL CODE FOR REVERSAL OF A NUMBER
#Time complexity = O(1) as it will take the same time independent of the number of digits 
#Space complexity = O(1) as it will occupy the same space independent of the number of characters 

def reverseNew (num):
    num = str(num)
    num = num[::-1] #reverse the string by stepping back by -1 from the end to the start of the string.
    return (num)