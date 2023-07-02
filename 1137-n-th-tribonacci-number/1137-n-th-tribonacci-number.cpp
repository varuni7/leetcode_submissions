class Solution {
public:
    int tribonacci(int n) {
        int t0=0;
        int t1=1;
        int t2=1;
        int ti=t0+t1+t2;
        for (int i=3;i<=n;i++)
        {
            ti=t1+t2+t0;
            t0=t1;
            t1=t2;
            t2=ti;
            
        }
        if (n ==0 )
        { return t0;}
        if (n==1 | n==2)
        {
            return 1;
        }
            
        return ti;
        
    }
};