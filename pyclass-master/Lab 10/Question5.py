# Wap a python program to implement a stack data structure using class and objects with push pop and traversal mathod
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)

    def traverse(self):
        print("Stack elements:")
        for item in reversed(self.items):
            print(item)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("Stack size:", stack.size())
stack.traverse()

print("Top element:", stack.peek())

print("Popped element:", stack.pop())
print("Popped element:", stack.pop())

print("Stack size after popping:", stack.size())
stack.traverse()


