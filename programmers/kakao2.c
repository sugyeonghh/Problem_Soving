#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int solution(const char* s) {
    int answer = 0;
    char* alpha[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    
    while (*s) {
        if (*s >= '0' && *s <= '9')
            answer = answer * 10 + *s++ - '0';
        else {
            for (int i = 0; ; i++) {
				if (!(strncmp(alpha[i], s, strlen(alpha[i])))) {
					answer = answer * 10 + i;
					s += strlen(alpha[i]);
					break ;
				}
			}
        }
    }
    return answer;
}

int main(void)
{
    char *s = "2three45sixseven";
    printf("%s\n", s);
    printf("answer: %d \n", solution(s));
}