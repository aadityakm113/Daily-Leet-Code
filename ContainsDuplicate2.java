//https://leetcode.com/problems/contains-duplicate-ii/description/
class ContainsDuplicate2 {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> window= new HashSet<>();
        int l=0;//initialize the left pointer
        for(int r=0;r<=nums.length-1;r++){
            if(r-l>k){//check the size of the window
                window.remove(nums[l]);//remove the left most value from the window(hashset)
                l++;//slide the window 
            }
            if(window.contains(nums[r])){//if the number is already in the hashset then the number is a duplicate
                return true;
            }
            window.add(nums[r]);//add the element to the hashset
        }
        return false;
    }
}