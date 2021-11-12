class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if (not root):
        return

    inorder(root.left)
    print(root.data)
    inorder(root.right)

def insert(root,data):

    if not root:
        root = Tree(data)
        return

    q = []
    q.append(root)
    while q:
        root = q[0]
        q.pop(0)
        if (not root.left):
            root.left = Tree(data)
            break
        else:
            q.append(root.left)

        if (not root.right):
            root.right = Tree(data)
            break
        else:
            q.append(root.right)







BT = Tree(8)
BTL = Tree(7)
BTR = Tree(6)
BTLL = Tree(7)
BTLR = Tree(3)
BTRL = Tree(9)
BTRR = Tree(1)

BT.left = BTL
BT.right = BTR
BT.left.left = BTLL
BT.left.left = BTLR
BT.right.left = BTRL
BT.right.right = BTRR

insert(BT,999)
inorder(BT)

