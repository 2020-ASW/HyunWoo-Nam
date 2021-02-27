import sys
from collections import defaultdict

read = sys.stdin.readline
n, m = map(int, read().strip().split())
cow_house = [-1 for _ in range(m + 1)]
adj = defaultdict(list)

for cow in range(n):
    adj[cow].extend(map(int, read().strip().split()[1:]))


def dfs(start):
    for nxt in adj[start]:
        if visit[nxt]:
            continue
        visit[nxt] = True

        if cow_house[nxt] == -1 or dfs(cow_house[nxt]):
            cow_house[nxt] = start
            return True
    return False


ans = 0
for cow in adj:
    visit = [False for _ in range(m + 1)]
    if dfs(cow):
        ans += 1
print(ans)
