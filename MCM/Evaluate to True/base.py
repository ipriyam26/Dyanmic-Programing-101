#User function Template for python3

class Solution:
    
    def solveForLeftOver(self,S: str,i:int,j:int,isTrue: bool):
        
        if i>j:
            return 0

        if i==j:
            if isTrue:
                return 1 if S[i]=="T" else 0
            else:
                return 1 if S[i]=="F" else 0
                
        ans = 0
        for k in range(i+1,j,2):
            
            lt = self.solveForLeftOver(S,i,k-1,True)
            lf = self.solveForLeftOver(S,i,k-1,False)

            rt = self.solveForLeftOver(S,k+1,j,True)
            rf = self.solveForLeftOver(S,k+1,j,False)

            if S[k] == '|':
                ans += lt*rt + lf*rt + lt*rf if isTrue else lf*rf
            elif S[k] == "&":
                ans += lt*rt if isTrue else lf*rf + lt*rf +rt*lf
            else:
                ans += lt*rf + rt*lf if isTrue else lf*rf + rt*lt
                
        return ans
    
    def countWays(self, N, S):
        
        return self.solveForLeftOver(S,0,N-1,True)

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