#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void	swap(char **s1, char **s2)
{
	char	*tmp;

	tmp = *s1;
	*s1 = *s2;
	*s2 = tmp;
}

int		main(void)
{
	int		num;
	int		min;
	char	**words;

	printf("how many words do you in: ");
	scanf("%d", &num);
	words = (char **)malloc(sizeof(char *) * num);
	for (int i = 0; i < num; i++)
	{
		words[i] = (char *)malloc(sizeof(char) * 50);
		scanf("%s", words[i]);
	}
	
	for ()

	printf("\n\n");
	for (int i = 0; i < num; i++)
		printf("%s\n", words[i]);
}
