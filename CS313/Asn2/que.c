
//#include "que.h"

struct node {
	int value;
	struct node *next;
};

struct que {
	struct node *head;
	struct node *tail;
	int count;
};

// declarations
struct que* create_que();
struct node* create_node(int value);
void enqueue(struct que *que, struct node *node);
int is_empty(struct que *que);
int dequeue(struct que *que);

struct que* create_que() {
	struct que *new_que;
	new_que = malloc(sizeof(struct que));
	new_que->head = NULL;
	new_que->tail = NULL;
	new_que->count = 0;
	return new_que;
}

struct node* create_node(int value) {
	struct node *new_node;
	new_node = malloc(sizeof(struct node));
	//~ if (new_node == NULL) {
		//~ puts("queue is full");
		//~ exit(EXIT_FAILURE);
	//~ }
	new_node->value = value;
	new_node->next = NULL;
	return new_node;
}

void enqueue(struct que *que, struct node *node) {
	if (is_empty(que))
		que->head = node;
	else
		que->tail->next = node;
	que->tail = node;
	que->count += 1;
}

int is_empty(struct que *que) {
	return que->head == NULL;
}

int dequeue(struct que *que) {
	struct node *next = que->head;
	if (que->head == que->tail)
		que->tail = NULL;
	que->head = que->head->next;
	que->count -= 1;
	return next->value;
}