def fibonacci_memo(n, memo={}):
    if n in memo:  # Check if the value is already computed
        return memo[n]
    if n <= 1:  # Base case
        return n
    # Recursive case with memoization
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

n = 100  # Number of terms you want in the Fibonacci sequence
for i in range(n):
    print(fibonacci_memo(i))