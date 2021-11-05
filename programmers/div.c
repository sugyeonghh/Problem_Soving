#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int div_(int num) {
    int cnt = 0;
    
    for (int i = 1; i < num / 2; i++) {
        if (num % i == 0)
            cnt++;
    }
    return cnt % 2;
}

int solution(int left, int right) {
    int answer = 0;
    
    for (int i = left; i <= right; i++) {
        answer += div_(i) == 1 ? -i : i;
    }
    
    return answer;
}

int main(void)
{
    printf("answer: %d \n", solution(13, 17));
}