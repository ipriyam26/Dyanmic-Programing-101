#User function Template for python3

class Solution:
    
    def findLongestCommonSubstring(self,S1,S2,n,m,count):
        if n==0 or m==0:
            return 0
        
        if self.dp[n][m]!=-1:
            return self.dp[n][m]
        
        if S1[n-1]==S2[m-1]:
            count =  self.findLongestCommonSubstring(S1,S2,n-1,m-1,count+1)
        
        count = max(count,self.findLongestCommonSubstring(S1,S2,n-1,m,0),self.findLongestCommonSubstring(S1,S2,n,m-1,0)) 
        
        
        return  count
        
        
    
    def longestCommonSubstr(self, S1, S2, n, m):
        self.dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        return self.findLongestCommonSubstring(S1,S2,n,m,0)

        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends