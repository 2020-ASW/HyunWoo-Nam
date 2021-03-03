def time_to_sec(time):
    h, m, s = map(int, time.split(":"))
    return h * 60 * 60 + 60 * m + s


def sec_to_time(sec):
    h = sec // 3600
    sec -= h * 3600
    m = sec // 60
    sec -= m * 60
    return "%02d:%02d:%02d" % (h, m, sec)


def solution(play_time, adv_time, logs):
    adv_sec = time_to_sec(adv_time)
    max_sec = time_to_sec("99:59:59") + 10
    user = [0 for _ in range(max_sec)]
    total_user = [0 for _ in range(max_sec)]
    prefix = [0 for _ in range(max_sec)]

    for log in logs:
        st, to = map(time_to_sec, log.split("-"))
        user[st] += 1
        user[to] += -1
    for i in range(1, max_sec):
        total_user[i] = user[i - 1] + total_user[i - 1]
    for i in range(1, max_sec):
        prefix[i] = total_user[i] + prefix[i - 1]
    tmp = 0
    for i in range(adv_sec, max_sec):
        if tmp < prefix[i] - prefix[i - adv_sec]:
            ans = i - adv_sec
            tmp = prefix[i] - prefix[i - adv_sec]
    return sec_to_time(ans)


ans = solution("02:03:55", "00:14:15",
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                "01:37:44-02:02:30"])
print(ans)

ans = solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
