
//include <iostream>
#include <stdio.h>
#include <stdlib.h>

// a point on the integer grid

struct Point
{  
  // data
  int x, y;
};

// constructor
// Point() {
// x = y = 0;
// }

void construct(struct Point* self) {
  self->x = 0;
  self->y = 0;
}

// add point componentwise
// void add(const Point &p) {
	// x += p.x;
	// y += p.y;
// }

void add(struct Point* self, struct Point* p) {
  self->x += p->x;
  self->y += p->y;
}
  
// print to standard output
// void print() const {
// std::cout << "(" << x << "," << y << ")" << std::endl;
// }

void print(struct Point* self) {
  printf("(%d,%d)\n", self->x, self->y);
}

int main()
{
  const int N = 100;
  //Point *a = new Point[N], sum;
  struct Point* a = malloc(sizeof(struct Point*) * N);
  if (!a) exit(1);
  int i = 0;
  for (; i < N; i++) 
    construct(&a[i]);
  struct Point sum = {0, 0};

  //for (int i=0; i < N; i++) {
  for (i = 0; i < N; i++) {
    //sum.add(a[i]);
    add(&sum, &a[i]);
  }
  //sum.print();
  print(&sum);
  //delete [] a;
  free(a);
  return 0;
}
