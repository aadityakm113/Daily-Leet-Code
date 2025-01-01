class MaxSumCircularSubarray {
    public int maxSubarraySumCircular(int[] nums) {
        int total = 0, curMax = 0, curMin = 0;
        int gloMax = nums[0], gloMin = nums[0];
        
        for (int n : nums) {
            curMax = Math.max(curMax + n, n); 
            gloMax = Math.max(gloMax, curMax); 
            
            curMin = Math.min(curMin + n, n);
            gloMin = Math.min(gloMin, curMin); 
            
            total += n; 
        }
        
        
        if (gloMax > 0) {
            return Math.max(gloMax, total - gloMin);
        } else {
            return gloMax;
        }
    }
}
