#include <stdio.h>
#include <string.h>

int main(void) {
	int t;

	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		char ps[51];
		int len = 0;
		int res = 0;

		scanf("%s", ps);
		len = strlen(ps);
		if (ps[len - 1] == '(')
			printf("NO\n");
		else {
			for (int top = len - 1; top >= 0; top--) {
				if (ps[top] == '(') res--;
				else if (ps[top] == ')') res++;
				if (res < 0) break;
			}
			if (res == 0) printf("YES\n");
			else printf("NO\n");			
		}
	}
	return 0;
}