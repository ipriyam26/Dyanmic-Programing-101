#User function Template for python3

from typing import List


class Solution:
    def subset_sum(self,sum_needed,n,wt):
        if sum_needed ==0:
            return True
        if n == 0:
            return False
        if self.dp[n][sum_needed]!=-1:
            return self.dp[n][sum_needed]
        
        if wt[n-1]>sum_needed:
            self.dp[n][sum_needed] = self.subset_sum(sum_needed,n-1,wt)
        else:
            self.dp[n][sum_needed] =self.subset_sum(sum_needed,n-1,wt) or self.subset_sum(sum_needed-wt[n-1],n-1,wt)
        return self.dp[n][sum_needed]
             
        
    def canPartition(self,arr:List[int]) -> bool:
        sum_arr = sum(arr)
        if int(sum_arr/2)!=sum_arr/2 or sum_arr%2==1:
            return False
        self.dp = [[-1 for _ in range(sum_arr+1)] for _ in range(len(arr)+1)]
        return True if sum_arr/2 in arr else self.subset_sum(int(sum_arr/2),len(arr),arr) 
        

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        wt = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.launch(wt))
# } Driver Code Ends