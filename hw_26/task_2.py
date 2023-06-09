# Task 3: Find if path is exists in graph

# https://leetcode.com/problems/find-if-path-exists-in-graph/

from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj = [[] for i in range(n)]

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        stack = [start]
        visited = set(stack)

        while stack:
            cur = stack.pop()

            if cur == end:
                return True

            for neighbor in adj[cur]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

        return False