import math
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
n = int(read().strip())
h = int(math.log2(n) + 1)
adj = defaultdict(list)
depth = [-1 for _ in range(n + 1)]
tree = [[-1 for _ in range(h)] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, read().strip().split())
    adj[a].append(b)
    adj[b].append(a)

m = int(read().strip())

q = deque([1])
depth[1] = 0

while q:
    x = q.popleft()

    for y in adj[x]:
        if depth[y] != -1:
            continue
        depth[y] = depth[x] + 1
        tree[y][0] = x
        q.append(y)

for j in range(1, h):
    for i in range(1, n + 1):
        if tree[i][j - 1] != -1:
            tree[i][j] = tree[tree[i][j - 1]][j - 1]


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(h - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = tree[b][i]

    if a == b:
        return a

    for i in range(h - 1, -1, -1):
        if tree[a][i] != tree[b][i]:
            a, b = tree[a][i], tree[b][i]

    return tree[a][0]


cur = 1
ans = 0

while m:
    nxt = int(read().strip())
    ans += depth[cur] + depth[nxt] - 2 * depth[lca(cur, nxt)]
    cur = nxt
    m -= 1
print(ans)
