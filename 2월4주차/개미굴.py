# https://www.acmicpc.net/problem/14725
import sys
from collections import defaultdict

read = sys.stdin.readline
n = int(read().strip())
bar = '--'


class Node(object):
    def __init__(self):
        self.child = defaultdict(Node)


class Tries(object):
    def __init__(self):
        self.head = Node()

    def add(self, words):
        cur = self.head
        for word in words:
            cur = cur.child[word]


def goAntCave(cur: Node, depth: int):
    if not Node:
        return

    for k, v in sorted(cur.child.items()):
        print(bar * depth + k)
        goAntCave(v, depth + 1)


tries = Tries()
while n:
    tries.add(read().strip().split()[1:])
    n -= 1

goAntCave(tries.head, 0)
