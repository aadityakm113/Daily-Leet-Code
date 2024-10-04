import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> set = new HashMap<>();
        //we are going to look at the hashmap to find the number which when added to nums[i] gives the target value
        for(int i=0;i<=nums.length;i++){
            int diff=target-nums[i]; //eg target=9, nums[0]=2. 9-2=7
            if(set.containsKey(diff)){//check to see if 7 is in the HashMap before adding the element to it
                return new int[] {set.get(diff),i};//returns the array containing the indices of the pair of numbers
            }
            set.put(nums[i],i);//add the value and index to the hashmap
        }
        return nums;
    }
}
