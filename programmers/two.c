#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int num[], size_t len) {
    int* answer;
    int sum[100*100 + 1];
    int cnt = 0;
    
    for (int i = 0; i <= 100*100; i++)
        sum[i] = 0;
    
    for (int i = 0; i < len; i++) {
        for (int j = i + 1; j < len - 1; j++) {
            int c = num[i] + num[j];
            sum[c] += 1;
            if (sum[c] == 1)
                cnt++;
        }
    }
    
    answer = (int*)calloc(cnt, sizeof(int));
    
    for (int i = 0; i <= 100*100; i++)
        if (sum[i])
            answer[i] = i;
    
    return answer;
}

int main(void)
{
	int arr[5] = {2,1,3,4,1};
    printf("answer: %d \n", solution(arr, 5));
}