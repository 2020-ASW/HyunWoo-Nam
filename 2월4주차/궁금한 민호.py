import sys
from copy import deepcopy

read = sys.stdin.readline
n = int(read().strip())
dp = [list(map(int, read().strip().split())) for _ in range(n)]
a = deepcopy(dp)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == k or j == k:
                continue
            if dp[i][j] == dp[i][k] + dp[k][j]:
                a[i][j] = 0
            if dp[i][j] > dp[i][k] + dp[k][j]:
                print(-1)
                sys.exit()

print(sum(map(sum, a)) // 2)
