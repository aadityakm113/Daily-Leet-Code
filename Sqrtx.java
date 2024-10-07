class Sqrtx {
    public int mySqrt(int x) {
        if(x==0||x==1)
            return x;
        int l=1;
        int r=x;
        int res=0;
        while(l<=r){
            int mid=l+(r-l)/2;
            if(mid==x/mid)
                return mid;
            else if(mid<x/mid){
                l=mid+1;
                res=mid;
            }
            else
                r=mid-1;
        }
        return res;
    }
}