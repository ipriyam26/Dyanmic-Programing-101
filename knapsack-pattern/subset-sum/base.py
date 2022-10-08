#User function Template for python3

class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def subset_sum(self,sum_needed,n,wt):
        if sum_needed ==0:
            return True
        if n==0:
            return False
        if sum_needed>wt[n-1]:
            return self.subset_sum(sum_needed,n-1,wt) or self.subset_sum(sum_needed-wt[n-1],n-1,wt)
        else:
            return  self.subset_sum(sum_needed,n-1,wt) 
    
    def equal_sum_partion(self,arr):
        sum_arr = sum(arr)/2
        if (int(sum_arr)!=sum_arr):
            return 0
        if sum_arr in arr:
            return 1
        res = self.subset_sum(sum_arr,len(arr),arr)
        if res:
            return 1
        return 0
        
        

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        sum_needed= int(input())
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.subset_sum(sum_needed=sum_needed,n=len(wt),wt=wt))
# } Driver Code Ends