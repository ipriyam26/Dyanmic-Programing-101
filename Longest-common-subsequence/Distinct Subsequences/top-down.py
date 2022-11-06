class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            self.dp[i][0]=1 
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    self.dp[i][j]= self.dp[i-1][j-1] + self.dp[i-1][j]

    def findDistinct(self,i:int,j:int,s:str,t:str) -> int:
        if j<0:
            return 1
        if i<0:
            return 0
        
        if s[i]==t[j]:
            return self.findDistinct(i-1,j-1,s,t) + self.findDistinct(i-1,j,s,t)
        else:
            return self.findDistinct(i-1,j,s,t)
if __name__ =="__main__" :
    sol = Solution()
    print(sol.numDistinct("babgbag","bag"))