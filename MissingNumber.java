// https://leetcode.com/problems/missing-number/
class MissingNumber {
    public int missingNumber(int[] nums) {
        
        int missing=-1;
        for(int i=0;i<=nums.length;i++){
            boolean found=false;
            for(int j=0;j<nums.length;j++){
                if(i==nums[j]){
                    found=true;
                    break;
                }
            }
            if(!found){
                missing=i;
                break;
            }
        }
        return missing;
    }
}