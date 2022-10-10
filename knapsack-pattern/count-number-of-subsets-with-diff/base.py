#User function Template for python3

from typing import List


class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def subset_sum(self,sum_needed,n,wt):
        if sum_needed ==0:
            return 1 
        if n == 0:
            return 0
        if(sum_needed<wt[n-1]):
            return self.subset_sum(sum_needed=sum_needed,n=n-1,wt=wt)
        
        return self.subset_sum(sum_needed,n-1,wt) + self.subset_sum(sum_needed-wt[n-1],n-1,wt)
    
    def runner(self,arr:)
             
        
        

if __name__ == '__main__':
    # test_cases = int(input())
    # for _ in range(test_cases):
        # sum_needed= int(input())
        # wt = list(map(int,input().strip().split()))
        ob=Solution()
        wt = [2,3,5,6,8,10]
        print(ob.subset_sum(sum_needed=10,n=len(wt),wt=wt))
# } Driver Code Ends