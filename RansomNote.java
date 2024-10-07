//https://leetcode.com/problems/ransom-note
import java.util.HashMap;
import java.util.Map;

public class RansomNote {
    public boolean canConstruct(String ransomNote, String magazine) {
        //Create HashMap to store the frequency of characters from the magazine array
        Map<Character,Integer> map = new HashMap<>();
        for(char c: magazine.toCharArray()){
            map.put(c,map.getOrDefault(c,0)+1); //increment the counter in the map
        }

        //check if the ransomNote can be constructed using the map
        for(char c : ransomNote.toCharArray()){
            //check if character is in the map or not
            if(!map.containsKey(c)||map.get(c)==0){
                return false;
            }
            //decrement character count
            map.put(c,map.get(c)-1);
        }
        return true;
    }
}
