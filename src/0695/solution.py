from collections import deque
from typing import List


class Solution:
    def _get_area(self, r, c, grid):
        q = deque()
        q.append((r, c))
        self.visited[r][c] = 1
        area = 0

        while q:
            area += 1
            r, c = q.popleft()

            if 0 <= r - 1 and r - 1 < self.m and grid[r - 1][c] and not self.visited[r - 1][c]:
                q.append((r - 1, c))
                self.visited[r - 1][c] = 1

            if 0 <= r + 1 and r + 1 < self.m and grid[r + 1][c] and not self.visited[r + 1][c]:
                q.append((r + 1, c))
                self.visited[r + 1][c] = 1

            if 0 <= c - 1 and c - 1 < self.n and grid[r][c - 1] and not self.visited[r][c - 1]:
                q.append((r, c - 1))
                self.visited[r][c - 1] = 1

            if 0 <= c + 1 and c + 1 < self.n and grid[r][c + 1] and not self.visited[r][c + 1]:
                q.append((r, c + 1))
                self.visited[r][c + 1] = 1

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        max_area = 0

        self.visited = []
        for _ in range(self.m):
            self.visited.append([0] * self.n)

        for r in range(self.m):
            for c in range(self.n):
                if grid[r][c] and not self.visited[r][c]:
                    max_area = max(max_area, self._get_area(r, c, grid))

        return max_area
