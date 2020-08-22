/*
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* returnSize){
    int* arr=(int*)malloc(sizeof(int)*(num+1));
    *returnSize = num+1;
    arr[0]=0;
    for(int i=1; i<num+1; i++){
        arr[i]=(i&1)?arr[i>>1]+1:arr[i>>1];
    }
    return arr;
}