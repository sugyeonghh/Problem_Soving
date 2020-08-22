int minAddToMakeValid(char * S){
    int result=0;
    int leftCnt=0;
    
    for(int i=0; i<strlen(S); i++){
        if(S[i]=='('){
            result++;
            leftCnt++;
        }
        else{
            if(leftCnt>0){
                result--;
                leftCnt--;
            }
            else
                result++;
        }
    }
    return result;
}
