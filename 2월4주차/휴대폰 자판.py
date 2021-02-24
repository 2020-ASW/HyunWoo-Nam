import sys
from collections import defaultdict

read = sys.stdin.readline


class Node(object):
    def __init__(self):
        self.child = defaultdict(Node)
        self.isEnd = False


class Tries(object):
    def __init__(self):
        self.head = Node()

    def add(self, word):
        cur = self.head
        for c in word:
            cur = cur.child[c]
        cur.isEnd = True

    def getCount(self, word):
        cur = self.head
        cnt = 0
        for i, c in enumerate(word):
            if i != 0 and len(cur.child) == 1:
                if i != len(word) and cur.isEnd:
                    cnt += 1
            else:
                cnt += 1
            cur = cur.child[c]
        return cnt


try:
    while True:
        n = int(read().strip())
        tries = Tries()
        words = []
        for _ in range(n):
            word = read().strip()
            words.append(word)
            tries.add(word)
        ans = 0
        for word in words:
            ans += tries.getCount(word)
        print("%.02f" % (round(ans / n, 2)))
except:
    pass