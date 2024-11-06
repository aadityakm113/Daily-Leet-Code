// https://leetcode.com/problems/running-sum-of-1d-array/
public class RunningSum1D {
    public int[] runningSum(int[] nums) {
        int runningSum=0;
        int[] res=new int[nums.length];
        for(int i = 0; i<nums.length;i++){
            runningSum+=nums[i];
            res[i]+=runningSum;
        }
        return res;
    } 
}
