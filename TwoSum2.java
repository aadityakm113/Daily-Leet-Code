// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
public class TwoSum2 {
    public int[] twoSum(int[] numbers, int target) {
        int l=0;
        int r=numbers.length-1;
        int[] res=new int[2];
        while(l<r){
            if(numbers[l]+numbers[r]<target){
                l++;
            }
            else if(numbers[l]+numbers[r]>target){
                r--;
            }
            else{
                res[0]=(l+1);
                res[1]=(r+1);
                return res;
            }
        }
        return res;
    }
}
