def solution(n, times):
    l, r = 0, max(times) * n
    while l < r:
        mid = (l + r) // 2
        cnt = 0
        for time in times:
            cnt += (mid // time)

        if cnt >= n:
            r = mid
        else:
            l += 1
    return r



