class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        dp = [[0] * cols for i in range(rows)]
        
        # set bottom and rigth most column and row to one as there is only one way to go 
        for i in range(cols) : 
            dp[rows-1][i] = 1

        for i in range(rows) : 
            dp[i][cols-1] = 1

        for r in range(rows-2,-1,-1)  :
            for c in range(cols-2,-1,-1)  :
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        
        return dp[0][0]
        