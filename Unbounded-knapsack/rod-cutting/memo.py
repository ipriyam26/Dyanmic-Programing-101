#User function Template for python3

class Solution:
    def knapSack(self,W, wt, val, N):
        self.dp =[[-1 for _ in range(W+1)] for _ in range(N+1)]
        # print(self.dp)
        return self.runner(W,wt,val,N)
        
    
    def runner(self,W, wt, val, N):
        if N==0 or W==0:
            return 0
        if self.dp[N][W]!=-1:
            return self.dp[N][W]
        
        if(wt[N-1]>W)  :
            self.dp[N][W]= self.runner(W=W,wt=wt,val=val,N=N-1)
        else:
            self.dp[N][W]=max(self.runner(W=W,wt=wt,val=val,N=N-1),
                   val[N-1]+self.runner(W=W-wt[N-1],wt=wt,val=val,N=N)
                   )
        return self.dp[N][W]
    
    def cutRod(self, price, n):
        wt = list(range(1,n+1))
        return self.knapSack(n,wt,price,n)

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends