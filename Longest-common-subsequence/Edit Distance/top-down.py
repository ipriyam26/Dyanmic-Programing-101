# @lc code=start
class Solution:
        
    def minDistance(self, word1: str, word2: str) -> int:
        self.dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        n,m = len(word1),len(word2)
        for j in range(m):
            self.dp[0][j]=j
        for i in range(n):
            self.dp[i][0]=i
        
        self.dp[0][0]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    self.dp[i][j] = self.dp[i-1][j-1]
                else:
                    self.dp[i][j] = 1+ min( self.dp[i-1][j],self.dp[i][j-1], self.dp[i-1][j-1])
        print(self.dp)
        return self.dp[n][m]
        