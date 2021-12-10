from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def isLetter(c):
            if ord("a") <= ord(c) <= ord("z"):
                return True
            if ord("A") <= ord(c) <= ord("Z"):
                return True
            return False

        results = []

        def perm(arr, i):
            if i == len(s):
                results.append("".join(arr))
            else:
                if isLetter(arr[i]):
                    arr[i] = arr[i].upper()
                    perm([c for c in arr], i + 1)
                    arr[i] = arr[i].lower()
                perm([c for c in arr], i + 1)

        arr = [c for c in s]
        perm(arr, 0)
        return results
