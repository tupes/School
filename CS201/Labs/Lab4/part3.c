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
	FILE * input = fopen("input3.txt", "r");
	long * ptr;
	int ii = 0;
	int jump = sizeof(long);
	int bytes = 10 * jump;
	char holder[MAX_DIGITS + 1];
	memset(holder, 0, MAX_DIGITS + 1);

	ptr = malloc(bytes);

	while (fgets(holder, MAX_DIGITS + 1, input) != NULL)
	{
		if (ii >= bytes)
		{
			bytes *= 2;
			ptr = realloc(ptr, bytes);
		}
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
