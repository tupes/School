
#include <stdlib.h>
#include "Grid.H"
using namespace std;

Grid::Grid(int w, int h) {
	width = w;
	height = h;
	open = new priority_queue<Grid::Node*, vector<Grid::Node*>, Grid::DereferenceCompareNode>;
	closed = new set<Grid::Node*>;
	tiles_ref = new vector< vector<Grid::Node*>* >;
	for (int y = 0; y < height; ++y) {
		tiles_ref->push_back(new vector<Grid::Node*>);
		//tiles.push_back(*(*(tiles_ref)[x]));
		for (int x = 0; x < width; ++x) {
			(*((*tiles_ref)[y])).push_back(new Grid::Node(x, y));
		}
	}
}

Grid::~Grid() {
	delete open;
	delete closed;
	for (int y = 0; y < height; y++) {
		for (int x = 0; x < width; ++x)
			delete (*(*tiles_ref)[y])[x];
		delete (*tiles_ref)[y];
	}
	delete tiles_ref;
}

int Grid::getWidth() const {
	return width;
}

int Grid::getHeight() const {
	return height;
}

int Grid::getEstimate(Grid::Node* from, Grid::Node* to) const {
	return abs(from->x - to->x) + abs(from->y - to->y);
}

Grid::Node* Grid::getNode(int x, int y) const {
	return (*(*tiles_ref)[y])[x];
}

Grid::Tile Grid::getTile(int x, int y) const {
	return (*getNode(x, y)).tile;
}

bool Grid::isConnected(int size, int x1, int y1, int x2, int y2) {
	return true;
}

int Grid::findShortestPath(int size, int x1, int y1, int x2, int y2, 
vector<Direction> &path) {
	Node* start = getNode(x1, y1);
	Node* goal = getNode(x2, y2);
	start->g = 0;
	start->h = getEstimate(start, goal);
	start->f = start->g + start->h;
	open->push(start);
	// search
	while (!open->empty()) {
		Node* next = open->top();
		if (next->x == x2 && next->y == y2) {
			// found shortest, save it in path
			return 1;
		}
		//~ for (int i = 0; i < next->numChildren(); ++i)
			//~ consider(next, next->children[i], goal);
		considerChildren(next, goal);
		
		closed->insert(next);
	}
	// no path
	return -1;
}

void Grid::considerChildren(Grid::Node* now, Grid::Node* goal) {
	bool w = false, e = false, n = false, s = false, nw = false, ne = false, sw = false, se = false; 
	// consider W
	if (now->x != 0 && now->tile == getTile(now->x - 1, now->y)) {
		w = true; nw = true; sw = true;
		consider(now, getNode(now->x - 1, now->y), goal);
	}
	// consider E
	if (now->x != width - 1 && now->tile == getTile(now->x + 1, now->y)) {
		e = true; ne = true; se = true;
		consider(now, getNode(now->x + 1, now->y), goal);
	}
	// consider N
	if (now->y != 0 && now->tile == getTile(now->x , now->y - 1)) {
		n = true; nw = true; ne = true;
		consider(now, getNode(now->x, now->y - 1), goal);
	}
	// consider S
	if (now->y != height - 1 && now->tile == getTile(now->x, now->y + 1)) {
		s = true; sw = true; se = true;
		consider(now, getNode(now->x , now->y + 1), goal);
	}
	// consider NW
	if ( && now->tile == getTile(now->x - 1, now->y)) {
		w = true; nw = true; sw = true;
		consider(now, getNode(now->x - 1, now->y), goal);
	}
	// consider E
	if (now->x != width - 1 && now->tile == getTile(now->x + 1, now->y)) {
		e = true; ne = true; se = true;
		consider(now, getNode(now->x + 1, now->y), goal);
	}
	// consider N
	if (now->y != 0 && now->tile == getTile(now->x , now->y - 1)) {
		n = true; nw = true; ne = true;
		consider(now, getNode(now->x, now->y - 1), goal);
	}
	// consider S
	if (now->y != height - 1 && now->tile == getTile(now->x, now->y + 1)) {
		s = true; sw = true; se = true;
		consider(now, getNode(now->x , now->y + 1), goal);
	}
}

void Grid::consider(Grid::Node* from, Grid::Node* now, Grid::Node* goal) {
	int newg = from->g + getCost(from, now);
	if (foundBetter(now, newg)) return;
	now->g = newg;
	now->h = getEstimate(now, goal);
	now->f = now->g + now->h;
	now->parent = from;
	closed->erase(now);
	// check to see if node's in open first
	open->push(now);
}

int Grid::getCost(Grid::Node* from, Grid::Node* to) const {
	return 0;
}

bool Grid::foundBetter(Grid::Node* now, int g) const {
	return false;
}

void Grid::setTile(int x, int y, Grid::Tile tile) {
	(*getNode(x, y)).tile = tile;
}

