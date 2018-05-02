def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x]=f(x)
        return memo[x]
    return helper

@memoize
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)


"""
memo = {0:1, 1:1}
def fibm(n):
    if n not in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]

"""

"""
def fibi(num):
    memo = [1,1]
    for i in range(2,num+1):
        memo.append(memo[i-1] + memo[i-2])

    print(memo)

"""
