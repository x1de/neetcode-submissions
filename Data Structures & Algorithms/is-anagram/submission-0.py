class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        d2 = {}
        for i in s:
            if i in s1:
                s1[i]+=1
            else:
                s1[i]=1
        
        for j in t:
            if j in d2:
                d2[j]+=1
            else:
                d2[j]=1

        return s1==d2