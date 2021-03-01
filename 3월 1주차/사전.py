import sys

read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
dp = [[[-1 for _ in range(105)] for _ in range(105)] for _ in range(205)]


def go(d, n_cnt, m_cnt):
    if d == n + m:
        dp[d][n_cnt][m_cnt] = 1
        return 1

    if dp[d][n_cnt][m_cnt] != -1:
        return dp[d][n_cnt][m_cnt]

    ret = 0
    if n_cnt > 0:
        ret += go(d + 1, n_cnt - 1, m_cnt)
    if m_cnt > 0:
        ret += go(d + 1, n_cnt, m_cnt - 1)
    dp[d][n_cnt][m_cnt] = ret
    return ret


def getAns(d, n_cnt, m_cnt, k, ans):
    if d == n + m:
        print(ans)
        sys.exit()

    left = 0
    if n_cnt > 0:
        left = dp[d + 1][n_cnt - 1][m_cnt]
        if left >= k:
            getAns(d + 1, n_cnt - 1, m_cnt, k, ans + 'a')
    if m_cnt > 0:
        getAns(d + 1, n_cnt, m_cnt - 1, k - left, ans + 'z')


go(0, n, m)
if dp[0][n][m] < k:
    print(-1)
else:
    getAns(0, n, m, k, '')

