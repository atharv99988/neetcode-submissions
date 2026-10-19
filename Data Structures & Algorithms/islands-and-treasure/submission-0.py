class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        queue = deque()

        for r in range(ROWS) : 
            for c in range(COLUMNS) :
                if grid[r][c] == 0 : 
                    queue.append((r,c))
        
        while queue : 

            r, c = queue.popleft()
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)] :
                nr , nc = r + dr, c + dc

                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLUMNS and grid[nr][nc] == 2147483647 :
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))

    
            
        
        

        