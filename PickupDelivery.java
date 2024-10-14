//https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/
public class PickupDelivery {
    class Solution {
        public int countOrders(int n) {
            long mod = 1000000007;
            long output = 1;
    
            for (int i = 1; i <= n; i++) {
                // There are i ways to place the pickup, and (2*i - 1) ways to place the delivery
                output = output * i * (2 * i - 1) % mod;
            }
    
            return (int) output;
        }
    }
    
}
