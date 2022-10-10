import itertools
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        #~ Main idea
        # The minimum difference between two subarray is ideally 0
        # , to find zero we need the two subarrays to be half, so try to find half
        # if we find half then min diff is zero else we find the min diff from half.
        sum_of_array = sum(nums)
        if(sum_of_array==0):return 0
        to_be_found=sum_of_array//2
        diff = self.findHalf(nums=nums,target=to_be_found,n=len(nums))
        
        found_half = to_be_found-diff
        other_half = sum_of_array-found_half
        return other_half-found_half
        
    def findHalf(self,nums: List[int],target:int,n:int) -> int:
        dp= [[None for _ in range(target+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=0
        for i in range(target+1):
            dp[0][i]=i
        for i, j in itertools.product(range(1,n+1), range(1,target+1)):
            dp[i][j] = dp[i-1][j] if j<nums[i-1] else min(dp[i-1][j],dp[i-1][j-nums[i-1]])
        return dp[n][target]
        
        

        # if target==0:
        #     return 0
        # if n==0:
        #     return target
        # if self.dp[n][target]:
        #     return self.dp[n][target]
        
        # if target<nums[n-1]:
        #     self.dp[n][target]= self.findHalf(nums,target,n-1)
        # else:
        #     self.dp[n][target]=min(self.findHalf(nums,target-nums[n-1],n-1),self.findHalf(nums,target,n-1))
        # return self.dp[n][target]