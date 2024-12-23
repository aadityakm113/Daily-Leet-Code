// https://leetcode.com/problems/add-strings/description/
class AddStrings{
    public String addStrings(String num1, String num2) {
        int i=num1.length()-1, j = num2.length()-1,carry=0,total;
        StringBuilder res= new StringBuilder();
        while(i>=0 || j>=0 || carry>0){
            int dig1= (i>=0?num1.charAt(i)-'0':0);
            int dig2= (j>=0?num2.charAt(j)-'0':0);
            total=dig1+dig2+carry;
            carry=total/10;
            res.append(total%10);
            i--;
            j--;
        }
        return res.reverse().toString();
    }
}