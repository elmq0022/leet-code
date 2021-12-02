class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_hash = [0] * 26
        for c in s1:
            s1_hash[ord(c) - ord("a")] += 1

        s2_hash = [0] * 26
        i, j = 0, 0

        while j < len(s1) - 1:
            s2_hash[ord(s2[j]) - ord("a")] += 1
            j += 1

        while j < len(s2):
            s2_hash[ord(s2[j]) - ord("a")] += 1

            if s1_hash == s2_hash:
                return True

            s2_hash[ord(s2[i]) - ord("a")] -= 1

            i += 1
            j += 1

        return False
