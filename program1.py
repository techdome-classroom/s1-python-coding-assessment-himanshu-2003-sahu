class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            # Check for invalid indices or if it's water ('W') or already visited
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or grid[r][c] == "W"
                or visited[r][c]
            ):
                return

            visited[r][c] = True  # Mark this landmass as visited

            # Explore the four directions (up, down, left, right)
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        island_count = 0

        # Iterate over each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find unvisited land ('L'), it's a new island
                if grid[r][c] == "L" and not visited[r][c]:
                    dfs(r, c)
                    island_count += 1  # Increment the island count

        return island_count


# Example usage:
solution = Solution()

grid1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]

grid2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]

print(solution.getTotalIsles(grid1))  # Output: 1
print(solution.getTotalIsles(grid2))  # Output: 3
