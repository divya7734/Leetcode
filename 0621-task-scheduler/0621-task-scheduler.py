class Solution(object):
    def leastInterval(self, tasks, n):
        cnt = [0] * 26
        for i in tasks: cnt[ord(i) - ord('A')] += 1
        mx, mxcnt = max(cnt), 0
        for i in cnt: 
            if i == mx: mxcnt += 1
        return max((mx - 1) * (n + 1) + mxcnt, len(tasks))
