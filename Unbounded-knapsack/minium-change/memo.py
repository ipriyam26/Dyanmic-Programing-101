#User function Template for python3

from typing import List


class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def launch(self,sum_needed,n,wt):
        self.dp= [[None for _ in range(sum_needed+1)] for _ in range(n+1)]
        return self.subset_sum(sum_needed=sum_needed,n=n,wt=wt,taken=0)
    
    def subset_sum(self,sum_needed,n,wt,taken):
        if sum_needed ==0:
            return taken
        if n==0:
            return 99999
        if self.dp[n][sum_needed]!=None:
            return self.dp[n][sum_needed]
        if wt[n-1]>sum_needed:
            self.dp[n][sum_needed]=  self.subset_sum(sum_needed,n-1,wt,taken)
        else:
            self.dp[n][sum_needed] =min(self.subset_sum(sum_needed,n-1,wt.taken),self.subset_sum(sum_needed-wt[n-1],n,wt,taken+1))
        return self.dp[n][sum_needed]

    def coinChange(self, coins, sum):
        if sum==0:
            return 0

        n = self.subset_sum(sum,len(coins),coins,0)
        return -1 if n==99999 else n
        
        

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # sum_needed= int(input())
        # wt = list(map(int,input().strip().split()))
        # ob=Solution()
        wt=[3,5,6,7,1,2]
        print(Solution().launch(sum_needed=7,n=len(wt),wt=wt))
# } Driver Code Ends