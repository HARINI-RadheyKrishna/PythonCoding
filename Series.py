#Code to print series of n numbers in the pattern 1/1! + 2/2! + ... + n/n!
#Time complexity = O(n) where n here represents the maximum value of the series
#Space complexity = O(1) since no extra space has been taken

def fact(n):
    if n >= 2:
        return n*fact(n-1)
    else:
        return 1

sum = 0.00
print("Hello world!")
seriesN = int(input())
for i in range(1, seriesN+1):
    out = fact(i)
    print (out)
    sum += float(i/out)
    
print("The output of the series of ", seriesN, " elements is ",sum)