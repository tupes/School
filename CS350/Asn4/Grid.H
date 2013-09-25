#ifndef GRID
#define GRID

// CMPUT 350 Assignment 4
// Due Wednesday Nov 7, 22:00
//  
// Submit your solution using astep like so:
//  
// astep -c c350 -p a4 README Grid.H Grid.C
//  
// Your submissions will be marked considering their correctness
// (syntax+semantics), documentation, efficiency, and coding style. Add
// assert statements to check important pre/post-conditions, use all
// warning options (-Wall). Your code must compile without warning or 
// error messages.
//
// Do not include a main() function in your submitted code. When testing,
// define your main() function in a separate .C file and link with it.

#include <vector>
#include <queue>
#include <set>
#include <functional>

// The objective of this assignment is to produce a class that can
// store a map-like structure and perform pathfinding and connectivity
// operations on it.
//
// Class Grid represents a rectangular tile map with octile topology,
// i.e. 8 compass directions using Euclidean distance. There are
// blocked, ground, or water tiles. Moving objects are not represented
// in the grid.
//
// The moving object for pathfinding has a location x,y and a size s.
// It is considered to occupy the tiles from x to x+s in the x-axis,
// and from y to y+s in the y-axis. Thus, an object with size 0
// occupies one tile, and object with size 1 occupies a 2x2 square,
// and an object with size 2 occupies a 3x3 square. You are only
// required to support objects of size 0 to 2.
//
// Moves are permitted if and only if all tiles passed through during
// the move have the same tile type. For instance, if a 3x3 object is
// on ground tiles, it may only move diagonally if the 4x4 region it
// passes over is composed solely of ground tiles.
//
// Similarly, a 2x2 object on water tiles may move to the east if the
// 3x2 region it passes over is composed entirely of water tiles.
//
// Example:
//
//   01234
//
// 0 wwggg   A 3x3 object centered in this 5x5 map may move west, south, or
// 1 ggggg   southwest, because it will pass only over ground tiles. However,
// 2 ggggg   it may NOT move northeast, even though it would wind up on a 3x3
// 3 ggggw   patch of ground tiles, because it would clip through some water
// 4 ggggw   tiles when moving.
//
// Note that in the above example, the object's initial location would
// be (1,1) and its size would be 2, meaning it occupies from 1 to 3
// on both the x and y axises.
//
// To test your implementation issue make which creates testGrid.
// See TestGrid.C for documentation.
//
// exampleGrid is our solution

class Grid
{
public: 

	enum Tile { GROUND, WATER, BLOCKED };

	enum Direction { N, NE, E, SE, S, SW, W, NW };

	static const int CARDINAL_COST = 100; // Cost to move in cardinal direction
	static const int DIAGONAL_COST = 141; // Cost to move diagonally

private:

	// todo: add private data members
	int height;
	int width;

	class Node {
	public:
		int x;
		int y;
		Tile tile;
		int f;
		int g;
		int h;
		int in_open;
		int in_closed;
		Node* parent;
		std::vector<Node*> children;
	
		Node(int x_arg, int y_arg) {
			x = x_arg;
			y = y_arg;
		}
		
		int numChildren() {
			return children.size();
		}
	};
		
	// slightly modified from a stack overflow post by rlbond
	struct DereferenceCompareNode : public std::binary_function<Node*, Node*, bool>
	{
	    bool operator()(const Node* lhs, const Node* rhs) const
	    {
		return lhs->f < rhs->f;
	    }
	};
	
	std::vector< std::vector<Node*>* > *tiles_ref;
	//std::vector< std::vector<Tile> > tiles;
	std::priority_queue<Node*, std::vector<Node*>, DereferenceCompareNode> *open;
	std::set<Node*> *closed;

public:

	Grid(int width, int height);
	~Grid();

	// Map properties
	int getWidth() const;
	int getHeight() const;
	int getEstimate(Node*, Node*) const;
	int getCost(Node*, Node*) const;
	bool foundBetter(Node*, int) const;
	Node* getNode(int x, int y) const;
	Tile getTile(int x, int y) const;

	// Pathfinding operations

	// Return true iff object with a given size can reside on (x1, y1)
	// and move from there to (x2, y2) while staying at the same tile
	// type without colliding. 
	//
	// This should execute faster than calling findShortestPath().
	// 
	// Also, iff the map hasn't changed, subsequent calls with the same
	// x1,y1,x2,y2 coordinates SHOULD BE MUCH FASTER. Hint: flood fill + caching
	bool isConnected(int size, int x1, int y1, int x2, int y2);

	// Compute a shortest path from (x1, y1) to (x2, y2) for an object
	// with a given size. Store the shortest path into path, and return
	// the cost of that path (using CARDINAL_COST for the moves N, E, S,
	// and W, and DIAGONAL_COST for the moves NE, SE, SW, and NW) or -1
	// if there is no path. Reduce initialization time by using the generation 
	// counter trick.
	int findShortestPath(int size, int x1, int y1, int x2, int y2, 
		       std::vector<Direction> &path);

	// Mutators
	void considerChildren(Node* next, Node* goal);
	void consider(Node*, Node*, Node*);
	void setTile(int x, int y, Tile tile);
};

#endif