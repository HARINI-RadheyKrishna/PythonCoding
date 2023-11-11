

def fibonacci(n):

    fib = [0,1]

    if n == 2:
        return fib
    elif n<=1:
        fib = [0]
        return fib
    else:
        while len(fib) < n:
            new = fib[-1] + fib[-2]
            fib.append(new)
        return fib

outp = fibonacci(3)
print (outp)