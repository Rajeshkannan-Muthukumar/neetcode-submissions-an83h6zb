class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,left=0,0
        bottom,right=len(matrix)-1,len(matrix[0])-1
        res=[]
        while left<=right and top <=bottom:
            for j in range(left,right+1):
                res.append(matrix[top][j])
            top+=1
            if left<=right:
                for i in range(top,bottom+1):
                    res.append(matrix[i][right])
                right-=1
            if top<=bottom:
                for k in range(right,left-1,-1):
                    res.append(matrix[bottom][k])
                bottom-=1
            
            if left<=right:
                for z in range(bottom,top-1,-1):
                    res.append(matrix[z][left])
                left+=1
        return res

        