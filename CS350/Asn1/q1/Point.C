
//include <iostream>
#include <stdio.h>

// a point on the integer grid

struct Point
{
  // constructor
  Point() {
    x = y = 0;
  }
  
  // data
  int x, y;
};

// add point componentwise
//~ void add(const Point &p) {
	//~ x += p.x;
	//~ y += p.y;
//~ }

void add(Point* self, Point* p) {
	self->x += p->x;
	self->y += p->y;
}
  
// print to standard output
//~ void print() const {
//~ std::cout << "(" << x << "," << y << ")" << std::endl;
//~ }

void print(Point* self) {
	printf("(%d,%d)\n", self->x, self->y);
}

int main()
{
  const int N = 100;
  Point *a = new Point[N], sum;

  //for (int i=0; i < N; i++) {
  int i = 0;
  for (; i < N; i++) {
    add(&sum, &a[i]);
  }
  //sum.print();
  print(&sum);
  delete [] a;
}