#User function Template for python3

class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, N):
        self.dp =[[-1 for _ in W+1] for _ in N+1]
        
    
    def runner(self,W, wt, val, N):
        if N==0 or W==0:
            return 0
        if self.dp[N][W]!=-1:
            return self.dp[N][W]
        
        if(wt[N-1]>W)  :
            self.dp[N][W]= self.runner(W=W,wt=wt,val=val,N=N-1)
        else:
            self.dp[N][W]=max(self.runner(W=W,wt=wt,val=val,N=N-1),
                   val[N-1]+self.runner(W=W-wt[N-1],wt=wt,val=val,N=N-1)
                   )
        return self.dp
        
        

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends