class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or grid[r][c] == "W"
                or visited[r][c]
            ):
                return

            visited[r][c] = True  

            
            dfs(r + 1, c)  
            dfs(r - 1, c)  
            dfs(r, c + 1)  
            dfs(r, c - 1)  

        island_count = 0

        
        for r in range(rows):
            for c in range(cols):
               
                if grid[r][c] == "L" and not visited[r][c]:
                    dfs(r, c)
                    island_count += 1  

        return island_count



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

print(solution.getTotalIsles(grid1)) 
print(solution.getTotalIsles(grid2))  
