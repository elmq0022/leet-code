from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = deque()
        m, n = len(image), len(image[0])

        color = image[sr][sc]
        if color == newColor:
            return image

        q.append((sr, sc))

        while q:
            r, c = q.popleft()

            if 0 <= r - 1 and r - 1 < m and image[r - 1][c] == color:
                q.append((r - 1, c))
            if 0 <= r + 1 and r + 1 < m and image[r + 1][c] == color:
                q.append((r + 1, c))
            if 0 <= c - 1 and c - 1 < n and image[r][c - 1] == color:
                q.append((r, c - 1))
            if 0 <= c + 1 and c + 1 < n and image[r][c + 1] == color:
                q.append((r, c + 1))

            image[r][c] = newColor

        return image
