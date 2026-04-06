class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title=""
        while columnNumber>26:
            rem=columnNumber%26
            add=90 if rem==0 else 64
            txt=chr(rem+add)
            title=txt+title
            sub=1 if rem==0 else 0
            columnNumber=(columnNumber//26)-sub
        title=chr(columnNumber+64)+title
        return title