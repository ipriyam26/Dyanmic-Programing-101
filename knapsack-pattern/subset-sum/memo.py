#User function Template for python3

from typing import List


class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def launch(self,sum_needed,n,wt):
        self.dp= [[None for _ in range(n+1)] for _ in range(sum_needed+1)]
        return self.subset_sum(sum_needed=sum_needed,n=n,wt=wt)
    
    def subset_sum(self,sum_needed,n,wt):
        if sum_needed ==0:
            return True
        if n==0:
            return False
        
        if self.dp[sum_needed][n]!=None: return self.dp[sum_needed][n]
            
        if sum_needed>wt[n-1]:
            self.dp[sum_needed][n] =self.subset_sum(sum_needed,n-1,wt) or self.subset_sum(sum_needed-wt[n-1],n-1,wt)
        else:
            self.dp[sum_needed][n]=  self.subset_sum(sum_needed,n-1,wt) 
        return self.dp[sum_needed][n]
        

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        sum_needed= int(input())
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.launch(sum_needed=sum_needed,n=len(wt),wt=wt))
# } Driver Code Ends