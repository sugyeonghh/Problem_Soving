#include <stdio.h>
#include <string.h>

int main(void)
{
	char	arr[100];
	int		cnt;

	scanf("%s", arr);
	cnt = strlen(arr);
	for (int i = 0; i < strlen(arr); i++)
	{
		if (((arr[i] == 'c') || (arr[i] == 's') || (arr[i] == 'z')) && (arr[i + 1] == '='))
			cnt--;
		else if ((arr[i] == 'c' || arr[i] == 'd') && arr[i + 1] == '-')
			cnt--;
		else if ((arr[i] == 'l' || arr[i] == 'n') && arr[i + 1] == 'j')
			cnt--;
		else if (arr[i] == 'd' && arr[i + 1] == 'z' && arr[i + 2] == '=')
			cnt--; 
	}
	printf("%d", cnt);
	return (0);
}
