#from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1, h2 = defaultdict(int), defaultdict(int)
        for ch in s:
            h1[ch]+=1
        for ch in t:
            h2[ch]+=1
        return h1==h2