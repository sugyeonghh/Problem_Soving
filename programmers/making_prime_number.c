#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int is_prime(int num) {
	if (num == 1)
		return 0;
	else if (num == 2)
		return 1;
	for (int p = 3; p < num; p++) {
		if (num % p == 0)
			return 0;
	}
	return 1;
}

int solution(int nums[], size_t len) {
    int answer = 0;
	int sum = 0, cnt = 0;
    
    for (int i = 0; i < len - 2; i++) {
		for (int j = i + 1; j < len - 1; j++) {
			for (int k = j + 1; k < len; k++) {
				if (is_prime(nums[i] + nums[j] + nums[k]))
					answer++;
			}
		}
	}
    return answer;
}