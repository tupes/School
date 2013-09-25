
//extern struct node;

struct node* create_node(int value);

void enqueue(struct que *que, struct node *node);
int is_empty(struct que *que);
int dequeue(struct que *que);