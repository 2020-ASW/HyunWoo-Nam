import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 5 + 1)
n = int(read().strip())
pows = [1 for _ in range(n)]
MOD = 1000000
for i in range(1, n):
    pows[i] = (pows[i - 1] * 2) % MOD

pos = [-1 for _ in range(n + 1)]
idx = 1
for e in map(int, read().strip().split()):
    for num in map(int, read().strip().split()):
        pos[num] = idx
    idx += 1


def hanoi(num, des):
    if num == 0:
        return 0

    ret = 0
    if pos[num] != des:
        ret = pows[num - 1]
        other = [e for e in range(1, 4) if e != pos[num] and e != des][0]
        ret = (ret + hanoi(num - 1, other)) % MOD
    else:
        ret = hanoi(num - 1, des)
    return ret


print(pos[n])
print(hanoi(n - 1, pos[n]))
