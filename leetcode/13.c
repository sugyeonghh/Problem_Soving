#define I 1
#define V 5
#define X 10
#define L 50
#define C 100
#define D 500
#define M 1000


int romanToInt(char *s){
    
    int     result = 0;
    int     num = 0;
    
    for (int i = 0; i < strlen(s); i++){
        if (s[i] == 'I')
            result += I;
        if (s[i] == 'V' || s[i] == 'X'){
            num = (s[i] == 'V') ? V : X;
            if (i > 0 && s[i - 1] == 'I')
                result += num - I * 2;
            else
                result += num;
        }
        else if (s[i] == 'L' || s[i] == 'C'){
            num = (s[i] == 'L') ? L : C;
            if (i > 0 && s[i - 1] == 'X')
                result += num - X * 2;
            else
                result += num;
        }
        else if (s[i] == 'D' || s[i] == 'M'){
            num = (s[i] == 'D') ? D : M;
            if (i > 0 && s[i - 1] == 'C')
                result += num - C * 2;
            else
                result += num;
        }
    }
    return (result);
}
