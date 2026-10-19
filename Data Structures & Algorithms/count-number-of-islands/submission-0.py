class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        cols = len(grid[0])
        rows = len(grid)

        visited = [[False for _ in range(cols)] for _ in range(rows)] 
        numberOfIslands = 0

        def dfs(r,c) : 
            if r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c] or grid[r][c] == '0': 
                return 
            else : 
                visited[r][c] = True
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == "1" and visited[r][c] == False : 
                    dfs(r,c)
                    numberOfIslands += 1

        return numberOfIslands 