from functools import lru_cache

@lru_cache(maxsize=None)#memorization
def fib_recur(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib_recur(n-1)+fib_recur(n-2))

def fib_iter(n):
    a,b=0,1
    for _ in range (n):
        a,b=b,a+b

    return a

    