import java.util.Stack;

public class ReversePolishNotation {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        String operators ="+-*/";
        for(String token:tokens){
            if(operators.indexOf(token)!=-1){
                int b = stack.pop();
                int a = stack.pop();
                int res=0;
                if(token.equals("+")){
                    res=a+b;
                }
                else if(token.equals("-")){
                    res=a-b;
                }
                else if(token.equals("*")){
                    res=a*b;
                }
                else if(token.equals("/")){
                    res=a/b;
                }
                stack.push(res);
            }
            else
                stack.push(Integer.parseInt(token));
        }
        return stack.peek();
    }
} 