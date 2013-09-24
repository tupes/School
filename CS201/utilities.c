#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define maxtokes 256
// my version of python's list.split() method.


int split(char *tokens[], const char line[])
{
	int lindex = 0, tindex = 0, tokecount = 0;
	
	while (line[lindex] == ' ')
		lindex++;

	while (line[lindex] != '\n' && line[lindex] != '\0')
	{
		while (line[lindex] == ' ')
			lindex++;
		//tokens[tokecount] = malloc(sizeof(int) * maxtokes);
		tindex = 0;
		while (line[lindex] != ' ' && line[lindex] != '\n' && line[lindex] != '\0')
		{
			//printf("%c\n", line[lindex]);
			tokens[tokecount][tindex] = line[lindex];
			tindex++;
			lindex++;
		}
		
		tokens[tokecount][tindex] = '\0';
		//printf("%s\n", tokens[tokecount]);
		tokecount++;
	}
	//printf("%d\n", tokecount);
	tokens[tokecount] = NULL;
	return tokecount;
}
