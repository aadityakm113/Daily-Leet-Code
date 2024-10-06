#https://leetcode.com/problems/top-k-frequent-elements/
#O(n) use hashmap and frequency array 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range (len(nums)+1)]#number of elements in the frequency array 

        for n in nums:
            count[n]=1+count.get(n,0)#incrementing the count if n is in the map. Default 0 if not in the map already
        for n,c in count.items():
            freq[c].append(n)#add n to the respective count
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        