# CHALLENGE LINK https://www.codewars.com/kata/sum-of-multiples
def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    if n > m:
        n, m = m, n
        return sum(x for x in range(m, n, m) if x < m)
    else:
        return sum(x for x in range(n, m, n) if x < m)