#User function Template for python3

class Solution:
    
    def solveForLeftOver(self,S: str,i:int,j:int,isTrue: bool,dp):
        
        if i>j:
            return 0

        if i==j:
            if isTrue:
                return 1 if S[i]=="T" else 0
            else:
                return 1 if S[i]=="F" else 0
                
        ans = 0
        
        if dp[i][j][int(isTrue)]!=-1:
            return dp[i][j][int(isTrue)]
        
            
        for k in range(i+1,j,2):
            
            if dp[i][k-1][1]!=-1:
                lt = dp[i][k-1][1]
            else:
                lt = self.solveForLeftOver(S,i,k-1,True,dp)
            if dp[i][k-1][0]!=-1:
                lf = dp[i][k-1][0]
            else:
                lf = self.solveForLeftOver(S,i,k-1,False,dp)
                
            

            if dp[k+1][j][1] !=-1:
                rt = dp[k+1][j][1]
            else:   
                rt = self.solveForLeftOver(S,k+1,j,True,dp)
            if dp[k+1][j][0] !=-1:
                rf = dp[k+1][j][0]  
            else: 
                rf = self.solveForLeftOver(S,k+1,j,False,dp)

            if S[k] == '|':
                ans += lt*rt + lf*rt + lt*rf if isTrue else lf*rf
            elif S[k] == "&":
                ans += lt*rt if isTrue else lf*rf + lt*rf +rt*lf
            else:
                ans += lt*rf + rt*lf if isTrue else lf*rf + rt*lt
        
            dp[i][j][int(isTrue)]=ans
        return ans
    
    def countWays(self, N, S):
        dp = [[[-1 for _ in range(2)]  for _ in range(N+1)]  for _ in range(N+1)] 
        return self.solveForLeftOver(S,0,N-1,True,dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends