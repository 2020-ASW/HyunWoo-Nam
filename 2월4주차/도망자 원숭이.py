# https://www.acmicpc.net/problem/1602
import sys
from collections import defaultdict

read = sys.stdin.readline
n, m, q = map(int, read().strip().split())

dogs = list(map(int, read().strip().split()))
dogs.insert(0, 0)
dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
cost = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

while m:
    a, b, c = map(int, read().strip().split())
    dp[a][b] = c
    dp[b][a] = c
    m -= 1

for k, x in sorted(enumerate(dogs), key=lambda x: x[1]):
    if k == 0:
        continue
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])
            cost[i][j] = min(dp[i][j] + max(dogs[k], dogs[i], dogs[j]), cost[i][j])

while q:
    st, to = map(int, read().strip().split())
    ans = cost[st][to]
    print(ans if ans != float('inf') else -1)
    q -= 1
