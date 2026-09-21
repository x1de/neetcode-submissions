class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            lst = [0]*26
            for ch in word:
                lst[ord(ch)-ord('a')]+=1
            hmap[tuple(lst)].append(word)
        return list(hmap.values())
        