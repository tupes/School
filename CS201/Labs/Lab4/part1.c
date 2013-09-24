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

#define MAX_LINES 100
#define MAX_DIGITS 256

int main()
{
	FILE * input = fopen("input1.txt", "r");
	long nums[MAX_LINES];
	int ii = 0;
	char holder[MAX_DIGITS + 1];
	memset(nums, -1, MAX_LINES);
	memset(holder, 0, MAX_DIGITS + 1);

	while (fgets(holder, MAX_DIGITS + 1, input) != NULL)
	{
		nums[ii] = atoi(holder);
		ii++;
		memset(holder, 0, MAX_DIGITS + 1);
	}
	
	for (ii -= 2; ii > -1; ii--)
	{
		printf("%ld\n", nums[ii]);
	}
	
	fclose(input);
	exit(EXIT_SUCCESS);

}
