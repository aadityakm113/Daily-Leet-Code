//https://leetcode.com/problems/third-maximum-number/
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

public class ThirdMaxNum {
    class Solution {
    public int thirdMax(int[] nums) {
        Set<Integer> uniqueNums = new HashSet<>();
        for(int num:nums){
            uniqueNums.add(num);
        }
        Integer[] uniqueArr=uniqueNums.toArray(new Integer[0]);
        Arrays.sort(uniqueArr,Collections.reverseOrder());
        if(uniqueArr.length<3){
            return uniqueArr[0];
        }
        else
            return uniqueArr[2];
    }
}
}
