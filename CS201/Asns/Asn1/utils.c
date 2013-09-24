#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (void)
{
	FILE *fp;
	char *line;
	char *array[1000];
	int counter = 0;
	int len = 0;
	int read;
	printf("ok\n");
	
	fp = fopen("input.txt", "r");
	if (fp == NULL)
	{
		printf("Could not open\n");
		exit(EXIT_FAILURE);
	}
	printf("ok again\n");
	while ((read = getline(&line, &len, fp)) != -1)
	{
		printf("check\n");
		strcpy(array[counter], line);
		counter++;
		printf("%s", line);
	}
	
	for (int x = 0; x < counter; x++)
	{
		printf("%s\n", array[x]);
	}		
	
	if (line)
		free(line);
	
	return 0;
	
}