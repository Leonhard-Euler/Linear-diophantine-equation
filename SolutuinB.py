import math

def solve(a, n):
    """Computes the number of nonnegative solutions (x) of the linear
    Diophantine equation
        a[0] * x[0] + ... a[N-1] * x[N-1] = n

    Theory: For natural numbers a[0], a[2], ..., a[N - 1], n, and j,
    let p(a, n, j) be the number of nonnegative solutions.

    Then one has:
        p(a, m, j) = sum p(a[1:], m - k * a[0], j - 1), where the sum is taken
        over 0 <= k <= floor(m // a[0])
    """
    print(a)
    def p(a, m, j):
        if j == 0:
            return int(m == 0)
        else:
            return sum([p(a[1:], m - k * a[0], j - 1)
                        for k in range(1 + m // a[0])])

    return p(a, n, len(a))

if __name__ == '__main__':
    print(solve([3, 2, 1, 1], 40)) # 2282
