//https://leetcode.com/problems/valid-anagram/
public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length())
            return false;
        int[] count=new int[26];//size of array is number of letters in the alphabet
        for(int i =0;i<s.length();i++){
            count[s.charAt(i)-'a']++;//we subtract 'a' to get the index position of the character
            count[t.charAt(i)-'a']--;
        }
        for(int c:count){
            if(c!=0){
                return false;
            }
        }
        return true;
        
    }    
}
// s= anagram t=nagaram
// 0 1 2 3 4 5 6 7 8 9 10 11 12 13
// a b c d e f g h i j k  l  m  n 
//count s.charAt(0)-a = a-a=0th index. this index is incremented/decremented everytime 'a' is found
//count s.charAt(1)-a = n-a-
