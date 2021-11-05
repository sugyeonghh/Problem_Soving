#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* word) {
    int answer = 0;
    char* alpha = "zottffssen";
    int len[10] = {4, 3, 3, 5, 4, 4, 3, 5, 5, 4};
    int p = 0;
    
    while (word[p]) {
        if (word[p] >= 'a' && word[p] <= 'z') {
            int num = 0, flag = 0;
            for (int i = 0; !flag; i++) {
                if (word[p] == alpha[i]) {
                    if (word[p] == 't')
                        num = word[p + 1] == 'w' ? 2 : 3;
                    else if (word[p] == 'f')
                        num = word[p + 1] == 'o' ? 4 : 5;
                    else if (word[p] == 's')
                        num = word[p + 1] == 'i' ? 6 : 7;
                    else 
                        num = i;
                    p += len[num];
                    flag = 1;
                }
            }
            answer = answer * 10 + num;
        }
        else 
            answer = answer * 10 + word[p++] - '0';
    }
    return answer;
}

int main(void)
{
    char *s = "one4seveneight";
    printf("%s\n", s);
    printf("answer: %d \n", solution(s));
}