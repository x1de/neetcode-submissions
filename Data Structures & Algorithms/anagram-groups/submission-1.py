class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            frq = [0]*26
            for ch in word:
                frq[ord(ch)-ord('a')]+=1
            res[tuple(frq)].append(word)
        return list(res.values())