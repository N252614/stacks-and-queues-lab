import random


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add an item to the end of the queue (FIFO)
        self.items.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        # Return the front item without removing it
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all customers up to and including the winner.
        Returns the winner's name.
        """
        if self.is_empty():
            return None

        winner_index = random.randint(0, len(self.items) - 1)
        winner = self.items[winner_index]

        # Remove everyone up to and including the winner
        for _ in range(winner_index + 1):
            self.dequeue()

        return winner