//https://leetcode.com/problems/maximum-average-subarray-i/
public class MaxAvgSubArray {
    class Solution {
        public double findMaxAverage(int[] nums, int k) {
            double max=-Double.MAX_VALUE;//use double for precision and -Double.MAX_VALUE to handle negative values better. Double.MIN_VALUE does not represent most negative values in the range of double values
            int start=0;//starting pointer
            double windowSum=0;
            for(int end=0;end<nums.length;end++){
                windowSum+=nums[end];
                if(end-start+1==k){//checks the size of the window
                    max=Math.max(max,windowSum/k);
                    windowSum-=nums[start];//removes the first number
                    start++;//adds the next number
                }
            }
            return max;
        }
    } 
}
