class Solution:
    def isValid(self, s: str) -> bool:
        stck=[]
        for i in s:
            if i == '(':
                stck.append(")")
            elif i=="[":
                stck.append("]")
            elif i=="{":
                stck.append("}")
            else:
                if stck and stck[-1]==i:
                    stck.pop()
                else:
                    return False
        if stck:
            return False
        return True