// https://leetcode.com/problems/stamping-the-sequence/
import java.util.ArrayList;
import java.util.List;

public class StampingTheSequence {
   public int[] movesToStamp(String stamp, String target) {
        char[] tChar = target.toCharArray();
        char[] sChar = stamp.toCharArray();
        int count=0;
        boolean[] visited = new boolean[tChar.length];
        List<Integer> res = new ArrayList<>();

        while(count!=tChar.length){
            boolean didChange=false;
            for(int i = 0; i<=tChar.length-sChar.length; i++){
                if(!visited[i]&& canReplace(tChar,i,sChar)){
                    count=replace(tChar,i,sChar.length,count);
                    visited[i]=true;
                    didChange=true;
                    res.add(i);
                    if(count==tChar.length)
                        break;
                }
            }
            if(!didChange)
                return new int[0];
        }
        int[] result = new int[res.size()];
        int k =0;
        for(int i =res.size()-1;i>=0;i--){
            result[k++]=res.get(i);
        }
        return result;
    }

    boolean canReplace(char[] tchar,int pos, char[] schar){
        for(int i =0; i < schar.length;i++){
            if(tchar[i+pos]!='?' && tchar[i+pos]!=schar[i])
                return false;
        }
        return true;
    }
    int replace(char[] tchar, int pos, int len,int count){
        for(int i=0;i<len;i++){
            if(tchar[i+pos]!='?'){
                tchar[i+pos]='?';
                count++;
            }
        }
        return count;
    } 
}
