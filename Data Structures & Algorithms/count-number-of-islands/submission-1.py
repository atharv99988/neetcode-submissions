class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        directions = [
            [0, 1],
            [1, 0],
            [-1, 0],
            [0, -1]
        ]

        visited = [[0] * COLUMNS for _ in range(ROWS)]
        islands = 0

        def dfs(r,c) : 
            if (r >= ROWS or 
                c >= COLUMNS  or
                c < 0 or r < 0 or 
                grid[r][c] == "0" or visited[r][c] == 1): 
                return 
            else :
                visited[r][c] = 1
                for a,b in directions : 
                    dfs(r+a, c+b)

        for r in range(ROWS) : 
            for c in range(COLUMNS) :
                if grid[r][c] == "1" and visited[r][c] == 0:
                    print('Calling DFS')
                    dfs(r,c)
                    islands += 1
        print(visited)

        return islands

        