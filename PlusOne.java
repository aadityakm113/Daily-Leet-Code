public class PlusOne {
    public int[] plusOne(int[] digits) {
        for(int i=digits.length-1;i>=0;i--){// traverse in the reverse order and increment the last digit
            if(digits[i]<9){
                digits[i]++;
                return digits;
            }
            digits[i]=0;//when i is equal to 9, change the digit to zero
        }
        int[] one= new int[digits.length+1];//eg[9,9,9] . we have to increase the size of the array so we create a new array of size n+1.
        one[0]=1;//first digit of the new number will be one 
        return one;
    } 
}
