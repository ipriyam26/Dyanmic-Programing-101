#User function Template for python3
from functools import cache
import itertools

class Solution:


    

    def longestPalindromeSubseq(self, S):
        
        @cache
        def rec(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            
            if s[l] == s[r]:
                return 2 + rec(l + 1, r - 1)
            else:
                return max(rec(l + 1, r), rec(l, r - 1))
            
        return rec(0, len(s) - 1)
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends