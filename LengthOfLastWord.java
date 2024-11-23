// https://leetcode.com/problems/length-of-last-word
class LengthOfLastWord{
    public int lengthOfLastWord(String s) {
        int count=0;
        int i=s.length()-1;
        while(s.charAt(i)==' '){
            i--;
        }
        while(i>=0 && s.charAt(i)!=' '){
            count++;
            i--;
        }
        return count;
    }
}