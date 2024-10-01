//https://leetcode.com/problems/group-anagrams/description/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GroupAnagrams {

    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();// hashmap that contains the sorted string as key and an array list of the original anagrams
        for(String str:strs){
            char[] sortedArr=str.toCharArray();
            Arrays.sort(sortedArr);
            String sortedString= String.valueOf(sortedArr);
            if(!map.containsKey(sortedString)){
                map.put(sortedString, new ArrayList<>()); //if the key does not exist in the map, add the key and create a new array list for that key
            }
            map.get(sortedString).add(str);//if the map already contains the sorted string as key, add the original string to the array list of anagrams
        }
        return new ArrayList<>(map.values());
    }
    
}
