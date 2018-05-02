"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
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
