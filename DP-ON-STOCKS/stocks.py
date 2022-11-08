from typing import List


class Solution:
    
    def stock(self,i:int,owned: bool,wt:List[int]):
        if i==len(wt):
            return 0
        
        if owned:
            return max(  wt[i]+self.stock(i+1,not owned,wt),self.stock(i+1,owned,wt))
        else:
            return max( -wt[i]+self.stock(i+1,not owned,wt), self.stock(i+1,owned,wt))
    
    def caller(self,wt:List[int]):
        self.dp = {}
        return self.stock(0,False,wt) 

        
        

if __name__=='__main__' :

    print(Solution().stock(0,False,[7,6,4,3,1]))