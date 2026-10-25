"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        pass

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        pass

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        pass

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        pass

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        pass


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        pass

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        pass

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        pass

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        pass

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        pass


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")
print("      test popping from an empty stack,")
print("      test peeking at an empty stack,")
print("      and verify a single-item stack becomes empty after removal.")

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
print("      test dequeuing from an empty queue,")
print("      test viewing the front of an empty queue,")
print("      and verify a single-item queue becomes empty after removal.")

if __name__ == "__main__":
    main()
# Unit 2 Discussion: Stacks and Queues

## Project Overview

For this assignment, I created a Python program that demonstrated how stacks and queues work. I used a customer support desk as my real-world example because it helped me understand how these two data structures handle information differently.

## Stack Implementation

I created a stack using a Python list. I implemented the push, pop, peek, and is_empty methods. The stack followed the Last-In, First-Out (LIFO) rule, meaning the most recently added item was removed first.

I used the stack to represent a history of actions at a support desk. When an action was undone, the program removed the most recent action first.

## Queue Implementation

I created a queue using Python's collections.deque. I implemented the enqueue, dequeue, front, and is_empty methods.

The queue followed the First-In, First-Out (FIFO) rule. I used customer support tickets to demonstrate how requests were processed in the order they arrived.

## Edge Case Testing

I tested what happened when the program attempted to remove an item from an empty stack or queue. I also tested viewing the top or front of an empty structure.

The program returned None for these empty operations instead of crashing.

I also created a stack and queue containing only one item. After removing that item, I checked that each structure was empty.

## Memory Usage

I learned that both stacks and queues used more memory as additional items were stored. Their overall space complexity was O(n), where n represented the number of stored items.

## Lessons Learned

This assignment helped me understand why the order of removing information matters. I also learned how to use Python lists and deques to manage information and how to handle empty structures without causing errors.

## How to Run the Program

I ran the Python file in IntelliJ IDEA using the Python plugin. The program displayed the stack and queue operations, including the LIFO and FIFO demonstrations and edge-case tests.