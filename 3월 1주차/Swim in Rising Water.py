from heapq import heappush, heappop

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


class Solution:
    def swimInWater(self, grid) -> int:
        n = len(grid)
        q = [(grid[0][0], 0, 0)]
        visit = [[float('inf') for _ in range(n)] for _ in range(n)]
        visit[0][0] = grid[0][0]

        while q:
            t, x, y = heappop(q)

            if visit[x][y] < t:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                nxt_t = max(grid[nx][ny], t)

                if nxt_t < visit[nx][ny]:
                    heappush(q, (nxt_t, nx, ny))
                    visit[nx][ny] = nxt_t
        return visit[n - 1][n - 1]


