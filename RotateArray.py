class Solution:
    # O(n)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%(len(nums))
        temp=[0]*len(nums)
        for i in range(len(nums)):
            temp[(i+k)%len(nums)]=nums[i]
        for i in range(len(nums)):
            nums[i]=temp[i]

    # O(1)
    class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        l,r=0,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l,r=0,k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l,r=k,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
    
    # O(1) with helper function
    class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
    def reverse(self,nums:List[int],l:int,r:int)-> None:
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        