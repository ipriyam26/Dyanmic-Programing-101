#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    
    def lcs(self, t1:str,t2:str, n:int, m:int)->int:
        if n==0 or m==0:
            return 0
        
        if t1[n-1]==t2[m-1]:
            return 1+ self.lcs(t1=t1,t2=t2,n=n-1,m=m-1)
        else:
            return max(self.lcs(t1,t2,n-1,m),self.lcs(t1,t2,n,m-1))
        # return self.dp[n][m]
        
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcs(t1=text1,t2=text2,n=len(text1),m=len(text2))

if __name__ == "__main__":
    print(Solution().longestCommonSubsequence("abc","def"))
    
        
# @lc code=end

