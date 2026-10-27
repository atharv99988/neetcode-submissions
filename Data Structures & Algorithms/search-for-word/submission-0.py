class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board :
            return False
        if not word : 
            return True

        ROWS = len(board)
        COLUMNS = len(board[0])
        visited = set()

        def bfs(r,c,i) : 
            if i >= len(word) : 
                return True

            if r >= ROWS or r < 0 or c >= COLUMNS or c < 0 or (r,c) in visited or board[r][c] != word[i]: 
                return False

            visited.add((r,c)) 

            result =  (
                bfs(r+1,c,i+1) or
                bfs(r-1,c,i+1) or
                bfs(r,c+1,i+1) or 
                bfs(r,c-1,i+1)
            )

            visited.remove((r,c))
            return result

        
        for r in range(ROWS) : 
            for c in range(COLUMNS)  :
                if board[r][c] == word[0] : 
                    if bfs(r,c,0) : 
                        return True

        return False
        