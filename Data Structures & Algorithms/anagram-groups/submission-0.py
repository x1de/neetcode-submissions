class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for wrd in strs:
            count = [0]*26
            for j in wrd:
                count[ord(j)-ord("a")]+=1
            map[tuple(count)].append(wrd)

        return list(map.values())
