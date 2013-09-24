//~ name:               Mark Tupala
//~ ONE Card number:    1188594
//~ Unix id:            tupala
//~ lecture section:    B1
//~ instructor's name:  Dr. Martin Muller
//~ lab section:        H02
//~ TA's name:          Aditya Bhargava

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_DIGITS 256

int main()
{
	FILE * input = fopen("input2.txt", "r");
	long lines = 0;
	long * ptr;
	int ii = 0;
	int jump = sizeof(long);
	char holder[MAX_DIGITS + 1];
	memset(holder, 0, MAX_DIGITS + 1);

	fgets(holder, MAX_DIGITS + 1, input);
	lines = atol(holder);
	ptr = malloc(lines * jump);
	memset(holder, 0, MAX_DIGITS + 1);

	while (fgets(holder, MAX_DIGITS + 1, input) != NULL)
	{
		ptr[ii] = atol(holder);
		ii += jump;
		memset(holder, 0, MAX_DIGITS + 1);
	}

	for (ii -= jump * 2; ii >= 0; ii -= jump)
	{
		printf("%ld\n", ptr[ii]);
	}
	
	free(ptr);
	fclose(input);
	exit(EXIT_SUCCESS);

}
