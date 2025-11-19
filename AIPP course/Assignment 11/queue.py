class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.items.pop(0)
    def is_empty(self):
        return not self.items

if __name__ == "__main__":
    q = Queue()
    while True:
        try:
            cmd = input("Command (enqueue/dequeue/is_empty/q): ").strip().split()
            if not cmd or cmd[0] == 'q':
                break
            if cmd[0] == 'enqueue' and len(cmd) > 1:
                q.enqueue(cmd[1])
                print(f"Enqueued: {cmd[1]}")
            elif cmd[0] == 'dequeue':
                print(f"Dequeued: {q.dequeue()}")
            elif cmd[0] == 'is_empty':
                print(f"Empty: {q.is_empty()}")
        except IndexError as e:
            print(f"Error: {e}")
