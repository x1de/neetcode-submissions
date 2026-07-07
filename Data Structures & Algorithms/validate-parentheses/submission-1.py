class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack = []
        hmap = {"]":"[", "}":"{",")":"("}
        for c in s:
            if c in hmap:
                if len(stack)>0:
                    if hmap[c]!=stack.pop():
                        return False
                else:
                    return False
            else:
                stack.append(c)
        return True if len(stack)==0 else False