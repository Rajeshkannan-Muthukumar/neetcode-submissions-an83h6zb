class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title=""
        while columnNumber>26:
            rem=columnNumber%26
            if rem==0:
                title="Z"+title
                columnNumber=(columnNumber//26)-1
            else:
                title=chr(rem+64)+title
                columnNumber=(columnNumber//26)
        title=chr(columnNumber+64)+title
        return title