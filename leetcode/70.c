int climbStairs(int n){
    int* a=(int*)malloc(sizeof(int)*(n+1));
    a[0]=0;
    for(int i=1; i<=n; i++){
        if(i==1 || i==2)
            a[i]=i;
        else
            a[i]=a[i-1]+a[i-2];
    }
    return a[n];
}