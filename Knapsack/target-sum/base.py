from typing import List


class Solution:
    
    def runner(self,arr: List[int],sum:int,n:int) -> int:
        
        if (n==0):
            return 1 if sum==self.target else 0

        if (n,sum) in self.hash:
            return self.hash[(n,sum)]
        
        self.hash[(n,sum)] = self.runner(arr,sum+arr[n-1],n-1)+self.runner(arr,sum-arr[n-1],n-1)
        return self.hash[(n,sum)]
        
        
        
    def targetSum(self,arr: List[int],target:int,n:int):
        self.target = target
        self.hash = {}
        self.runner(arr,0,len(arr))
        
if __name__ == "__main__":
    arr = [1,1,1,1,1]
    s = 3
    print(Solution().targetSum(arr,s,len(arr)))
    