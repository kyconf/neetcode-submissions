class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: return 0

        rows, cols = len(grid), len(grid[0])

        
        islands = 0

        def dfs(r,c):
            
            if (r in range(rows) and c in range(cols) and grid[r][c] == '1'):
                grid[r][c] = '0'
               
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

            

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == '1'):
                    dfs(r,c)
                    islands += 1

        return islands
                    
      