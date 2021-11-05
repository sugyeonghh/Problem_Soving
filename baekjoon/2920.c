#include <stdio.h>

int main(void) {
	int arr[8];
	int asce, desc;


	for (int i = 0; i < 8; i++)
		scanf("%d", arr + i);
	asce = desc = 0;
	for (int i = 0; i < 7; i++) {
		if (arr[i] < arr[i + 1])
			asce++;
		else
			desc++;
	}
	if (asce == 7)
		printf("ascending\n");
	else if (desc == 7)
		printf("descending\n");
	else
		printf("mixed\n");
	return 0;
}