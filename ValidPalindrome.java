//https://leetcode.com/problems/valid-palindrome

// Solution 1
public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        String x="";
        String rev="";
        for(int i=0;i<s.length();i++){
            if (Character.isLetterOrDigit(s.charAt(i))){
                x+=Character.toLowerCase(s.charAt(i));
            }
        }
        for(int i=x.length()-1;i>=0;i--){
            rev+=x.charAt(i);
        }
        if(x.equals(rev)){
            return true;
        }
        else{
            return false;
        }
    }
}

//Solution 2 Use StringBuilder
class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder x = new StringBuilder();
        for(int i =0;i<s.length();i++){
            char c = s.charAt(i);
            if(Character.isLetterOrDigit(c)){
                x.append(Character.toLowerCase(c));
            }
        }
        return x.toString().equals(x.reverse().toString());
    }
}