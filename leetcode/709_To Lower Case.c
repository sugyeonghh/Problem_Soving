char * toLowerCase(char * str){
    for(int i=0; i<strlen(str); i++)
        if(str[i]>='A' && str[i]<='Z')
            str[i]+=32;
    return str;
}