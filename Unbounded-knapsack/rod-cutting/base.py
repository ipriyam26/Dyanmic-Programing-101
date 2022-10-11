#User function Template for python3

class Solution:
    def knapSack(self,W, wt, val, N):
        if N==0 or W==0:
            return 0
        if(wt[N-1]>W)  :
            return self.knapSack(W=W,wt=wt,val=val,N=N-1)
        return max(self.knapSack(W=W,wt=wt,val=val,N=N-1),
                   val[N-1]+self.knapSack(W=W-wt[N-1],wt=wt,val=val,N=N)
                   )

    def cutRod(self, price, n):
        wt = list(range(1,n+1))
        return self.knapSack(n,wt,price,n)
        #code here
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