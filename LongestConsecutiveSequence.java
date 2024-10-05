//https://leetcode.com/problems/longest-consecutive-sequence/
import java.util.Arrays;

public class LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        if(nums.length==0)
            return 0;
        Arrays.sort(nums);
        int count=1;
        int max=1;
        for(int i=0;i<nums.length-1;i++){
            if(nums[i]==nums[i+1]) //if the two number are equal, carry on
                continue;
            if(nums[i+1]==nums[i]+1)//increase counter if the two numbers are consecutive
                count++;
            else{
                max=Math.max(count,max);
                count=1;//reset counter if there is a gap. counter starts when consecutive number sequence is found again in the array
            } 
        }
        return Math.max(max,count);
    }
}
