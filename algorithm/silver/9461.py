T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0] * max(n+1, 6)
    dp[1:4] = [1,1,1]
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[n])
