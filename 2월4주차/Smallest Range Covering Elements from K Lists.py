# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
from heapq import heappush, heappop


def smallestRange(nums):
    q = []
    n = len(nums)
    max_num = -float('inf')
    for i in range(n):
        heappush(q, (nums[i][0], i, 0))
        max_num = max(max_num, nums[i][0])

    ans = (q[0][0], max_num)
    while True:
        num, nums_idx, idx = heappop(q)

        if idx == len(nums[nums_idx]) - 1:
            break

        next_num = nums[nums_idx][idx + 1]
        max_num = max(max_num, next_num)
        heappush(q, (next_num, nums_idx, idx + 1))

        if max_num - q[0][0] < ans[1] - ans[0]:
            ans = (q[0][0], max_num)
    return list(ans)


ans = smallestRange(nums=[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
print(ans)
