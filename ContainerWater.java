// https://leetcode.com/problems/container-with-most-water/description/
public class ContainerWater {
    public int maxArea(int[] height) {
        int l=0;
        int r=height.length-1;
        int res=0;
        int area=0;
        while(l<r){
            area=Math.min(height[l],height[r])*(r-l);
            res=Math.max(area,res);
            if(height[l]<height[r])
                l++;
            else
                r--;
        }
        return res;
    }
}
