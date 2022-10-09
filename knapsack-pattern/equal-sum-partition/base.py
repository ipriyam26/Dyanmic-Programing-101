#User function Template for python3

from typing import List


class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def subset_sum(self,sum_needed,n,wt):
        if sum_needed ==0:
            return True
        if n == 0:
            return False
        if wt[n-1]>sum_needed:
            return  self.subset_sum(sum_needed,n-1,wt)
        else:
            return self.subset_sum(sum_needed,n-1,wt) or self.subset_sum(sum_needed-wt[n-1],n-1,wt)
             
        
    def canPartition(self,arr:List[int]) -> bool:
        sum_arr = sum(arr)
        if int(sum_arr/2)!=sum_arr/2 or sum_arr%2==1:
            return False
        return True if sum_arr/2 in arr else self.subset_sum(sum_arr/2,len(arr),arr) 


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # sum_needed= int(input())
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.canPartition(arr=wt))
# } Driver Code Ends