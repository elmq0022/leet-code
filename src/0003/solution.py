class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        _set = set()
        p1 = p2 = 0
        max_val = 0

        while p2 < len(s):
            while p2 < len(s) and s[p2] not in _set:
                _set.add(s[p2])
                p2 += 1

            max_val = max(max_val, p2 - p1)

            while p2 < len(s) and s[p2] in _set:
                _set.remove(s[p1])
                p1 += 1

        return max_val
