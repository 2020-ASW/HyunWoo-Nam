import sys

read = sys.stdin.readline
n = int(read().strip())
solutions = list(map(int, read().strip().split()))
solutions.sort()
total = float('inf')
ans = None

for i, e in enumerate(solutions):
    l, r = i + 1, n - 1
    while l < r:
        tmp = e + solutions[l] + solutions[r]

        if abs(tmp) < total:
            total = abs(tmp)
            ans = solutions[i], solutions[l], solutions[r]

        if tmp > 0:
            r -= 1
        else:
            l += 1

for e in ans:
    print(e, end=' ')
