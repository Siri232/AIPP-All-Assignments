class Node:
    def __init__(self,v):
        self.v,self.l,self.r=v,None,None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,v):
        def f(n,v):
            if not n:return Node(v)
            if v<n.v:n.l=f(n.l,v)
            elif v>n.v:n.r=f(n.r,v)
            return n
        self.root=f(self.root,v)
    def _in(self,n):
        if n:
            yield from self._in(n.l)
            yield n.v
            yield from self._in(n.r)
    def inorder_traversal(self):
        print(*self._in(self.root))

if __name__=="__main__":
    t=BST()
    while True:
        c=input("1.Insert 2.Inorder 3.Exit\n")
        if c=="1":t.insert(int(input("Value: ")))
        elif c=="2":t.inorder_traversal()
        elif c=="3":break

