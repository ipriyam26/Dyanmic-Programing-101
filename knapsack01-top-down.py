#User function Template for python3

class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, N):
        dp = [[-1 for _ in range(W+1)] for _ in range(N+1)]

        for i in range(N+1):
            dp[i][0]=0
        for i in range(W+1):
            dp[0][i]=0

        for i, j in itertools.product(range(1,N+1), range(1,W+1)):
            dp[i][j] = dp[i - 1][j] if (wt[i - 1] > W) else max(dp[i - 1][j], val[i - 1] + dp[i - 1][j - wt[i - 1]])
        
        

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends