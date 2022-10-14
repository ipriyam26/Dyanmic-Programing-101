#User function Template for python3

from typing import List


class Solution:
    #Function to return max value that can be put in knapsack of capacity W.

    def runner(self,arr:List[int],diff:int):
        to_be_found = (sum(arr)+diff)/2
        return self.launch(to_be_found,len(arr),arr)
    
    def launch(self,sum_needed,n,wt):
        self.dp= [[None for _ in range(sum_needed+1)] for _ in range(n+1)]
        return self.subset_sum(sum_needed=sum_needed,n=n,wt=wt)
    
    def subset_sum(self,sum_needed,n,wt):
        if sum_needed ==0:
            return 1
        if n==0:
            return 0
        if self.dp[n][sum_needed]!=None:
            return self.dp[n][sum_needed]
        if wt[n-1]>sum_needed:
            self.dp[n][sum_needed]=  self.subset_sum(sum_needed,n-1,wt)
        else:
            self.dp[n][sum_needed] =self.subset_sum(sum_needed,n-1,wt) + self.subset_sum(sum_needed-wt[n-1],n-1,wt)
        return self.dp[n][sum_needed]
        

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # sum_needed= int(input())
        # wt = list(map(int,input().strip().split()))
        # ob=Solution()
        wt=[3,5,6,7,1,2]
        print(Solution().launch(sum_needed=7,n=len(wt),wt=wt))
# } Driver Code Ends