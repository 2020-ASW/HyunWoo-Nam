# https://programmers.co.kr/learn/courses/30/lessons/72415
from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations

directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


def bfs(start, end, board):
    x, y = start
    q = deque()
    q.append((x, y, 0))
    visit = [[False for _ in range(4)] for _ in range(4)]
    visit[x][y] = True

    while q:
        x, y, d = q.popleft()

        if (x, y) == end:
            return d

        for dx, dy in directions:
            nx, ny, nd = x + dx, y + dy, d + 1

            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or visit[nx][ny]:
                continue

            q.append((nx, ny, nd))
            visit[nx][ny] = True

        for i, direction in enumerate(directions):
            dx, dy = direction
            nx, ny, nd = x + dx, y + dy, d + 1
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                continue

            while 0 <= nx < 4 and 0 <= ny < 4 and not board[nx][ny]:
                nx += dx
                ny += dy

            nx = min(max(nx, 0), 3)
            ny = min(max(ny, 0), 3)

            if not visit[nx][ny]:
                q.append((nx, ny, nd))
                visit[nx][ny] = True
    return 0


def solution(board, r, c):
    q = deque()
    cards = defaultdict(list)
    for i in range(4):
        for j, e in enumerate(board[i]):
            if e:
                cards[e].append((i, j))

    ret = float('inf')
    for element in permutations(cards.keys()):
        tmp = 0
        board_cp = deepcopy(board)
        prev = (r, c)
        for e in element:
            tmp1, tmp2 = 0, 0

            st, to = cards[e]
            tmp1 += bfs(prev, st, board_cp)
            tmp1 += (bfs(st, to, board_cp) + 2)

            tmp2 += bfs(prev, to, board_cp)
            tmp2 += (bfs(to, st, board_cp) + 2)
            if tmp1 < tmp2:
                prev = to
            else:
                prev = st
            board_cp[st[0]][st[1]] = 0
            board_cp[to[0]][to[1]] = 0
            tmp += min(tmp1, tmp2)
        ret = min(tmp, ret)
    return ret


ans = solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)
print(ans)
ans = solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1)
print(ans)
