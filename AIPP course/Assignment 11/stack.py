class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.items[-1]
    def is_empty(self):
        return not self.items
if __name__ == "__main__":
    s = Stack()
    while True:
        try:
            cmd = input("Command (push/pop/peek/is_empty/q): ").strip().split()
            if not cmd or cmd[0] == 'q':
                break
            if cmd[0] == 'push' and len(cmd) > 1:
                s.push(cmd[1])
                print(f"Pushed: {cmd[1]}")
            elif cmd[0] == 'pop':
                print(f"Popped: {s.pop()}")
            elif cmd[0] == 'peek':
                print(f"Peek: {s.peek()}")
            elif cmd[0] == 'is_empty':
                print(f"Empty: {s.is_empty()}")
        except IndexError as e:
            print(f"Error: {e}")

