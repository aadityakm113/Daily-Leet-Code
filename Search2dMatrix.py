# O(mlogn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            l=0
            r=len(i)-1
            while l<=r:
                mid=(l+r)//2
                if target<i[mid]:
                    r=mid-1
                elif target>i[mid]:
                    l=mid+1
                else:
                    return True
        return False
    
O(logm)+O(logn)=O(logmn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])

        top,bottom=0,ROWS-1
        while top<=bottom:
            row=(top+bottom)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bottom=row-1
            else:
                break
        if not (top<=bottom):
            return False
        row=(top+bottom)//2
        l,r=0,COLS-1
        while l<=r:
            mid=(l+r)//2
            if target<matrix[row][mid]:
                r=mid-1
            elif target>matrix[row][mid]:
                l=mid+1
            else:
                return True
        return False
