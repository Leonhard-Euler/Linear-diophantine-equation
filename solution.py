import math

def solve(a, n):
    # dp[i][j] 表示 使用了 前 j 项系数, sum 为 i 的 等式个数, 那么答案就是dp[n][len(a) - 1]
    dp = [[0] * len(a) for _ in range(n+1)]
    dp[0] = [1]*len(a)
    for i in range(1, n+1):
        for j, c in enumerate(a):
            s1, s2 = 0, 0
            if j > 0:
                s1 = dp[i][j-1]
            if i >= c:
                s2 = dp[i-c][j]
            dp[i][j] = s1 + s2
    return dp[n][len(a)-1]


if __name__ == "__main__":
    print(solve([1, 1], 0))  # 1
    print(solve([1, 1], 1))  # 2
    print(solve([1, 1], 2))  # 3
    print(solve([1, 1], 3))  # 4
    print(solve([1, 1, 1, 1], 30)) # 5456
