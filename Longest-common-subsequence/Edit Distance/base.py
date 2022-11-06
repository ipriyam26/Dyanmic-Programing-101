class Solution:
    def findMinium(self,i:int,j:int,word1:str,word2:str):
        if i<0:
            return 0 if j<0 else 1+ self.findMinium(i,j-1,word1=word1,word2=word2)
        if j<0:
            return 1 + self.findMinium(i-1,j,word1=word1,word2=word2)

        if word1[i]==word2[j]:
            return self.findMinium(i-1,j-1,word1=word1,word2=word2)
        else:
            return  1 + min(self.findMinium(i-1,j,word1=word1,word2=word2) , self.findMinium(i,j-1,word1=word1,word2 = word2), self.findMinium(i-1,j-1,word1=word1,word2=word2))
        
        
    
    def minDistance(self, word1: str, word2: str) -> int:
        return self.findMinium(len(word1)-1,len(word2)-1,word1,word2)
