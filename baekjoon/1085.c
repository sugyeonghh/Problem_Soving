#include <stdio.h>
#include <math.h>

int main(void) {
	int x, y, w, h;
	int tmp[4] = {0, };
	int res;

	scanf("%d %d %d %d", &x, &y, &w, &h);
	tmp[0] = sqrt(pow(w - x, 2));
	tmp[1] = sqrt(pow(h - y, 2));
	tmp[2] = sqrt(pow(x, 2));
	tmp[3] = sqrt(pow(y, 2));
	res = tmp[0];
	for (int i = 1; i < 4; i++) {
		if (res > tmp[i])
			res = tmp[i];
	}
	printf("%d\n", res);
	return 0;
}