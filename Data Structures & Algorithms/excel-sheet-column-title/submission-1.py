class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title=""
        while columnNumber>26:
            rem=columnNumber%26
            txt=chr(rem+64)
            title=txt+title
            columnNumber=columnNumber//26
        txt=chr(columnNumber+64)
        title=txt+title
        return title