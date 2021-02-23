from collections import defaultdict


def solution(words, queries):
    class Node(object):
        def __init__(self):
            self.isEnd = False
            self.childSize = defaultdict(int)
            self.child = defaultdict(Node)

    class Tries(object):
        def __init__(self):
            self.head = Node()

        def add(self, word):
            cur = self.head
            w_len = len(word)
            for i, e in enumerate(word):
                cur.childSize[w_len - i] += 1
                cur = cur.child[e]
            cur.isEnd = True

        def find(self, query):
            cur = self.head
            for i, e in enumerate(query):
                if e == '?':
                    return cur.childSize[len(query) - i]
                else:
                    cur = cur.child[e]

            return 1

    tries = Tries()
    reverse_tries = Tries()
    ret = []
    for word in words:
        tries.add(word)
        reverse_tries.add(word[::-1])

    for query in queries:
        if query[0] == '?':
            ret.append(reverse_tries.find(query[::-1]))
        else:
            ret.append(tries.find(query))
    return ret


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?"])
