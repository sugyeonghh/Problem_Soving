int findJudge(int N, int** trust, int trustSize, int* trustColSize){
    int* arr=(int*)malloc(sizeof(int)*(N+1));
    int result=-1;
    
    for(int i=0; i<N+1; i++)
        arr[i]=0;
    
    for(int i=0; i<trustSize; i++){
        arr[(trust[i][0])]--;
        arr[(trust[i][1])]++;
    }
    
    for(int i=1; i<N+1; i++){
        if(arr[i]==N-1)
            result=i;
    }
    return result;
    
}