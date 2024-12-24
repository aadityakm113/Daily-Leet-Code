import java.util.Collections;
import java.util.PriorityQueue;

public class KthLargestEleArray {
   class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int i:nums){
            pq.offer(i);
        }
        for(int i=0;i<k-1;i++){
            pq.remove();
        }
        return pq.peek();
    }
} 
}
