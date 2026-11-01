
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Structure of a linked list node
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// STACK
typedef struct {
    Node* top;
} Stack;

// QUEUE
typedef struct {
    Node* front;
    Node* rear;
} Queue;


// Initialize Stack
void initStack(Stack* stack) {
    stack->top = NULL;
}

// Check if Stack is empty
bool stack_is_empty(Stack* stack) {
    return stack->top == NULL;
}

// Push a value onto Stack
bool push(Stack* stack, int value) {
    Node* newNode = malloc(sizeof(Node));

    if (newNode == NULL) {
        return false;
    }

    newNode->data = value;
    newNode->next = stack->top;
    stack->top = newNode;

    return true;
}

// Remove the top value from Stack
bool pop(Stack* stack, int* value) {
    if (stack_is_empty(stack)) {
        return false;
    }

    Node* temp = stack->top;
    *value = temp->data;

    stack->top = temp->next;
    free(temp);

    return true;
}

// Inspect the top value
bool peek(Stack* stack, int* value) {
    if (stack_is_empty(stack)) {
        return false;
    }

    *value = stack->top->data;
    return true;
}

// Free all remaining Stack nodes
void freeStack(Stack* stack) {
    int value;

    while (pop(stack, &value)) {
    }
}


// Initialize Queue
void initQueue(Queue* queue) {
    queue->front = NULL;
    queue->rear = NULL;
}

// Check if Queue is empty
bool queue_is_empty(Queue* queue) {
    return queue->front == NULL;
}

// Add a value to Queue
bool enqueue(Queue* queue, int value) {
    Node* newNode = malloc(sizeof(Node));

    if (newNode == NULL) {
        return false;
    }

    newNode->data = value;
    newNode->next = NULL;

    if (queue_is_empty(queue)) {
        queue->front = newNode;
        queue->rear = newNode;
    } else {
        queue->rear->next = newNode;
        queue->rear = newNode;
    }

    return true;
}

// Remove the first value from Queue
bool dequeue(Queue* queue, int* value) {
    if (queue_is_empty(queue)) {
        return false;
    }

    Node* temp = queue->front;
    *value = temp->data;

    queue->front = temp->next;

    if (queue->front == NULL) {
        queue->rear = NULL;
    }

    free(temp);

    return true;
}

// Inspect the first value
bool front(Queue* queue, int* value) {
    if (queue_is_empty(queue)) {
        return false;
    }

    *value = queue->front->data;
    return true;
}

// Free all remaining Queue nodes
void freeQueue(Queue* queue) {
    int value;

    while (dequeue(queue, &value)) {
    }
}


// MAIN PROGRAM
int main() {
    Stack stack;
    Queue queue;

    int value;

    initStack(&stack);
    initQueue(&queue);

    printf("=== STACK TEST ===\n");

    printf("Is empty: %s\n",
           stack_is_empty(&stack) ? "Yes" : "No");

    printf("Peek empty: %s\n",
           peek(&stack, &value) ? "Success" : "Empty");

    printf("Pop empty: %s\n",
           pop(&stack, &value) ? "Success" : "Empty");

    // Add one value
    push(&stack, 10);
    peek(&stack, &value);
    printf("Peek one value: %d\n", value);

    pop(&stack, &value);
    printf("Removed: %d\n", value);

    // Add several values
    push(&stack, 4);
    push(&stack, 7);
    push(&stack, 2);

    printf("Stack removal order: ");

    while (pop(&stack, &value)) {
        printf("%d ", value);
    }

    printf("\n");

    // Add a value again after removing everything
    push(&stack, 9);
    pop(&stack, &value);
    printf("Added again and removed: %d\n", value);

    freeStack(&stack);


    printf("\n=== QUEUE TEST ===\n");

    printf("Is empty: %s\n",
           queue_is_empty(&queue) ? "Yes" : "No");

    printf("Front empty: %s\n",
           front(&queue, &value) ? "Success" : "Empty");

    printf("Dequeue empty: %s\n",
           dequeue(&queue, &value) ? "Success" : "Empty");

    // Add one value
    enqueue(&queue, 10);
    front(&queue, &value);
    printf("Front one value: %d\n", value);

    dequeue(&queue, &value);
    printf("Removed: %d\n", value);

    // Add several values
    enqueue(&queue, 4);
    enqueue(&queue, 7);
    enqueue(&queue, 2);

    printf("Queue removal order: ");

    while (dequeue(&queue, &value)) {
        printf("%d ", value);
    }

    printf("\n");

    // Add a value again after removing everything
    enqueue(&queue, 9);
    dequeue(&queue, &value);
    printf("Added again and removed: %d\n", value);

    freeQueue(&queue);

    printf("\nAll tests completed.\n");

    return 0;
}
