//https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution {
    public int removeDuplicates(int[] nums) {
        int l=1;
        for(int r =1;r<nums.length;r++){
            if(nums[r]!=nums[r-1]){ //new number found
            nums[l]=nums[r];
            l++;
            }
        }
        return l;
    }
}