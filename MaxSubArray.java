// https://leetcode.com/problems/maximum-subarray/
public class MaxSubArray {
    public int maxSubArray(int[] nums) {
        int curSum=0;
        int maxSub=nums[0];
        for(int n : nums){
            if(curSum<0)
                curSum=0;
            curSum+=n;
            maxSub=Math.max(maxSub,curSum);
        }
        return maxSub;
    }
}
