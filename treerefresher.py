class tree:
    def __init__(self,data):
        self.data= data
        self.left= None
        self.right= None
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)    
def postorder(root):
    if root is None:
        return
    inorder(root.left)
    inorder(root.right) 
    print(root.data)    
def preorder(root):
    if root is None:
        return
    print(root.data) 
    inorder(root.left)
    inorder(root.right) 

def treesize(root):
    if root is None:
        return 0
    else:
        return(1+ treesize(root.left)+ treesize(root.right))

BT = tree(1)
BTL = tree(2)
BTR = tree(8)
BTLL = tree(7)
BTLR = tree(20)
BTRL = tree(18)
BTRR = tree(80)
BT.left = BTL
BT.right = BTR
BT.left.left = BTLL
BT.left.right = BTLR
#inorder(BT)
print(treesize(BT))

