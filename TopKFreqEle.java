//https://leetcode.com/problems/top-k-frequent-elements/
class TopKFreqEle{
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();//HashMap to store the count of each number
        for(int num : nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        PriorityQueue<Map.Entry<Integer,Integer>> pq= new PriorityQueue<>((a,b)->b.getValue()-a.getValue());
        for( Map.Entry entry : map.entrySet()){
            pq.add(entry);
        }
        int[] output= new int[k];
        for(int i=0; i<k;i ++){
            output[i]=pq.poll().getKey();
        }
        return output;

    }
}