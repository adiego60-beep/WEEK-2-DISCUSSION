# Unit 2 Discussion: Stacks and Queues

## Project Overview

For this assignment, I created a Python program to demonstrate how stacks and queues work. I used a customer support desk as my real-world example because it helped me understand how both data structures organize information differently.

## Stack Implementation

I created a stack using a Python list. I implemented the push, pop, peek, and is_empty methods.

The stack followed Last-In, First-Out (LIFO), meaning the most recently added item was removed first. I used this structure to keep track of support desk actions that could be undone.

I added four actions and removed them in reverse order to demonstrate LIFO behavior.

## Queue Implementation

I created a queue using Python's collections.deque. I implemented the enqueue, dequeue, front, and is_empty methods.

The queue followed First-In, First-Out (FIFO), meaning the first item added was the first item removed.

I used four customer support tickets to demonstrate how requests were processed in the order they arrived.

## Edge Case Testing

I tested what happened when I tried to remove an item from an empty stack or queue. I also tested viewing the top of an empty stack and the front of an empty queue.

The program returned None instead of crashing.

I also tested a stack and queue containing only one item. After removing the item, I verified that each structure was empty.

## Memory Usage

Both data structures used O(n) space because memory usage increased as more items were added.

The Python list supported stack operations, while collections.deque allowed items to be added to the back and removed efficiently from the front of the queue.

## Running the Program

I ran the Python program in Visual Studio Code. I checked the output to confirm that the stack followed LIFO, the queue followed FIFO, and the empty-structure tests worked correctly.

## Lessons Learned

This assignment helped me understand why choosing the correct data structure matters. I learned how stacks and queues handle information differently and why checking for empty structures is important to prevent errors.
