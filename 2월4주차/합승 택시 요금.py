from collections import defaultdict
from heapq import heappush, heappop


def dijkstra(adj, st, n):
    visit = [float('inf') for _ in range(n + 1)]
    visit[st] = 0
    q = [(0, st)]

    while q:
        cost, cur = heappop(q)

        if visit[cur] < cost:
            continue

        for nxt, nw in adj[cur].items():
            nxtCost = nw + cost
            if visit[nxt] > nxtCost:
                heappush(q, (nxtCost, nxt))
                visit[nxt] = nxtCost
    return visit


def solution(n, s, a, b, fares):
    adj = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for c, d, f in fares:
        adj[c][d] = f
        adj[d][c] = f

    common = dijkstra(adj, s, n)
    ret = float('inf')
    for i in range(1, n + 1):
        another = dijkstra(adj, i, n)
        cost = another[a] + common[i] + another[b]
        ret = min(ret, cost)
    return ret
