class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.findDistinct(len(s)-1,len(t)-1)
    
    def findDistinct(self,i:int,j:int,s:str,t:str) -> int:
        if j<0:
            return 1
        if i<0:
            return 0
        
        if s[i]==t[j]:
            return self.findDistinct(i-1,j-1,s,t) + self.findDistinct(i-1,j,s,t)
        else:
            return self.findDistinct(i-1,j,s,t)
if __name__ =="__main__" :
    sol = Solution()
    print(sol.numDistinct("babgbag","bag"))