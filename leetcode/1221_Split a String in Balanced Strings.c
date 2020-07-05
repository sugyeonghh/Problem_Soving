int balancedStringSplit(char * s){
    int Rcount=0, Lcount=0;
    int result=0;
    
    for(int i=0; i<strlen(s); i++){
        if(s[i]=='R')
            Rcount++;
        else
            Lcount++;
        if(Rcount==Lcount){
            result++;
            Rcount=0;
            Lcount=0;
        }
    }
    return result;
}