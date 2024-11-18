public class Search2dMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        for(int[] i:matrix){
            int l=0;
            int r=i.length-1;
            while(l<=r){
                int mid = (l+r)/2;
                if(target<i[mid])
                    r=mid-1;
                else if(target>i[mid])
                    l=mid+1;
                else
                    return true;
            }
        }
        return false;
    } 
}
