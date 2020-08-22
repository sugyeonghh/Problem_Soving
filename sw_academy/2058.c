#include <stdio.h>
#include <string.h>

main(){
    char *arr;
   	int result=0;
   scanf("%s",arr);
	for(int i=0; ;i++){
        if(arr[i]=='\0')
            break;
     //   printf("%5d", arr[i]-48);
        result+=arr[i]-48;
    }
    printf("%d", result);
}