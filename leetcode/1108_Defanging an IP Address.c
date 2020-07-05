char * defangIPaddr(char * address){
    char* result=(char*)malloc(sizeof(char)*strlen(address)*2);
    int num=0; 
    
    for(int i=0; i<strlen(address); i++){
        if(address[i]=='.'){
            result[num++]='[';
            result[num++]=address[i];
            result[num++]=']';
        }else{
            result[num++]=address[i];
        }
    }
    result[num]='\0';
    return result;
}