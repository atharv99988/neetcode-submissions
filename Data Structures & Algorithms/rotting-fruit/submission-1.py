class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        minutes = 0

        for r in range(ROWS) :
            for c in range(COLUMNS) :
                if grid[r][c] == 2 : 
                    queue.append((r,c))

        while queue :
            nodes = len(queue)
            for i in range(nodes) : 
                r,c = queue.popleft()
                for dr,dc in [(-1,0), (1,0), (0,1), (0,-1)] : 
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLUMNS and grid[nr][nc] == 1 :
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
            if queue : 
                minutes += 1
        
        for r in range(ROWS) :
            for c in range(COLUMNS) :
                if grid[r][c] == 1 : 
                    return -1
        
        return minutes
