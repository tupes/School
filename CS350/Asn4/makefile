all: testGrid

test: testGrid
	./testGrid

clean:
	rm -f ./testGrid

testGrid: TestGrid.C Grid.C Grid.H
	g++ -O3 -Wall -Wextra Grid.C TestGrid.C -L/usr/X11R6/lib -lglut -lGL -o ./testGrid

tar:
	rm -f a4.tar
	tar cf a4.tar *

submit:
	astep -c c350 -p a4 README Grid.C Grid.H
