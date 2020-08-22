#include <stdio.h>

main(){
	int n; 
    int max=0;
    int arr[10];
    scanf("%d",&n);

    for(int i=0; i<n; i++){
        for(int j=0; j<10; j++){
            scanf("%d",&arr[j]);
            if(max<arr[j])
                max=arr[j];
        }
        printf("#%d %d \n",i+1, max);
        max=0;
    }
}

