// https://leetcode.com/problems/jump-game/
class JumpGame{
    public boolean canJump(int[] nums) {
        int len=nums.length;
        int d = len-1;
        for(int i=len-2;i>=0;i--){
            if(nums[i]+i>=d)
                d=i;
        }
        return d==0;
    }
}