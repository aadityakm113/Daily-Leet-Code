//https://leetcode.com/problems/happy-number/
import java.util.HashSet;
import java.util.Set;

public record HappyNumber() {
    public boolean isHappy(int n) {
        Set <Integer> visited = new HashSet<>();
        if(n==1)
            return true;
        while(!visited.contains(n)){
            visited.add(n);
            n=sumOfSquares(n);
            if(n==1)
                return true;
        }
        return false;
    }
    public int sumOfSquares(int n){
        int sum=0;
        while(n>0){
            int digit=0;
            digit=(n%10)*(n%10);//using Math.pow() would lead to Type Mismatch error
            sum+=digit;
            n/=10;
        }
        return sum;
    }
}
