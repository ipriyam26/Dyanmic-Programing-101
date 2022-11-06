class Solution:
    def findMinium(self,i:int,j:int,word1:str,word2:str):
        #base condition
        if i<0 and j<0:
            return 0
        if i<0:
            return 1+i 
        if j<0:
            return 1 + j
                
        if self.dp[i][j]!=-1:
            return self.dp[i][j]
        
        if word1[i]==word2[j]:
            self.dp[i][j]= self.findMinium(i-1,j-1,word1=word1,word2=word2)
        else:
            self.dp[i][j]=  1 + min(self.findMinium(i-1,j,word1=word1,word2=word2) , self.findMinium(i,j-1,word1=word1,word2 = word2), self.findMinium(i-1,j-1,word1=word1,word2=word2))
        return self.dp[i][j]
        

    def minDistance(self, word1: str, word2: str) -> int:
        self.dp = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        return self.findMinium(len(word1)-1,len(word2)-1,word1,word2)

        