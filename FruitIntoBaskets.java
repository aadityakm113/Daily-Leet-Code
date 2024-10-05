//https://leetcode.com/problems/fruit-into-baskets/
import java.util.HashMap;
import java.util.Map;

public class FruitIntoBaskets {
   public int totalFruit(int[] fruits) {
        Map<Integer,Boolean> map = new HashMap<>();
        int max=0;
        int start=0;
        for(int end=0;end<fruits.length;end++){
            int type=fruits[end];
            if(map.size()<2&&!map.containsKey(type)){
                map.put(type,true);
                max=Math.max(max,end-start+1);
            }
            else if(map.containsKey(type)){
                max=Math.max(max,end-start+1);
            }
            else{
                // Map<Integer,Boolean> newMap = new HashMap<>(); Create a new hashmap
                // newMap.put(fruits[end-1],true);
                // newMap.put(type,true);
                map.clear();//map cleared to accommodate the new type
                map.put(fruits[end-1],true);//prev type added
                map.put(type,true);//current type added
                start=end-1;//start pointer is adjusted
                while(fruits[start]==fruits[start-1]){
                    start--;//used to adjust the window size if same type preceeds the current type
                }
                // map=newMap; used to assign the new map values to the original map if new map is created
                max=Math.max(max,end-start+1);
            }
        }
        return max;
    } 
}
