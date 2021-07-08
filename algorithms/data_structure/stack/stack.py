class Stack:
    def __init__(self):
        self.stack = list()

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise ValueError("No element!")

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)

