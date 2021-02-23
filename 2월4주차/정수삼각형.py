def solution(triangle):
    n = len(triangle)
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    def go(d, x):
        if d == n:
            return 0
        if dp[d][x] != -1:
            return dp[d][x]

        ret = 0
        for i in range(x, x + 2):
            ret = max(go(d + 1, i) + triangle[d][i], ret)
        dp[d][x] = ret
        return ret

    tmp = go(1, 0) + triangle[0][0]
    return tmp


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
