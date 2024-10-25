//https://leetcode.com/problems/jump-game-ii
public class JumpGame2 {
    public int jump(int[] nums) {
        //we perform a simplified 1D BFS 
        int res=0;
        int l=0;
        int r=0; //l and r represent the portion of the array to be used for bfs
        while (r<nums.length-1){
            int farthest=0;
            for(int i=l;i<r+1;i++){
                farthest=Math.max(farthest,nums[i]+i);
            }
            l=r+1;
            r=farthest;
            res++;
        }
        return res;
    } 
}
