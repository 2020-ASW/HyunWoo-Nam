import math
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
n = int(read().strip())
tree = defaultdict(list)
max_h = int(math.log2(n)) + 1
dp = [[-1 for _ in range(max_h)] for _ in range(n + 1)]
depth = [-1 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, read().strip().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque()
q.append(1)
depth[1] = 0

while q:
    cur = q.popleft()

    for nxt in tree[cur]:
        if depth[nxt] == -1:
            depth[nxt] = depth[cur] + 1
            dp[nxt][0] = cur
            q.append(nxt)

for j in range(1, max_h):
    for i in range(1, n + 1):
        if dp[i][j - 1] != -1:
            dp[i][j] = dp[dp[i][j - 1]][j - 1]


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(max_h - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = dp[b][i]

    if a == b:
        return a

    for i in range(max_h - 1, -1, -1):
        if dp[a][i] != dp[b][i]:
            a = dp[a][i]
            b = dp[b][i]

    return dp[a][0]


m = int(read().strip())

while m:
    a, b = map(int, read().strip().split())
    print(lca(a, b))
    m -= 1
