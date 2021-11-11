class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

newBt = TreeNode('Drink')
leftchild = TreeNode('hot')
rightchild = TreeNode('cold')
newBt.left =   leftchild
newBt.right = rightchild
leftleft = TreeNode('chink')
leftright = TreeNode('link')
newBt.left.left = leftleft
newBt.left.right = leftright

def preorder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorder(rootNode.left)    
    preorder(rootNode.right)

def postorder(rootNode):
    if not rootNode:
        return
    preorder(rootNode.left)    
    preorder(rootNode.right) 
    print(rootNode.data)   

def inorder(rootNode):
    if not rootNode:
        return
    preorder(rootNode.left)   
    print(rootNode.data)   
    preorder(rootNode.right) 
   

preorder(newBt)
print("----------")
inorder(newBt)
