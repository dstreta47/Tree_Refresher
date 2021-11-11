class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

newBT = TreeNode('Drinks')
hot = TreeNode('hot')
cold = TreeNode('cold')
newBT.left = hot
newBT.right = cold
tea = TreeNode('tea')
coffee = TreeNode('coffee')
hot.left = tea
hot.right = coffee

def preorder(root):
    if not root:
        return
    print(root.data)
    preorder(root.left) 
    preorder(root.right)   

def postorder(root):
    if not root:
        return
    preorder(root.left) 
    preorder(root.right)    
    print(root.data)  

def inorder(root):
    if not root:
        return
    preorder(root.left) 
    print(root.data)  
    preorder(root.right)   

def levelorder(root):
    if not root:
        return
    else:
        queue = []
        queue.append(root)
        while queue:
            print(queue[0].data)
            root = queue.pop(0)

            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)    


def search_BT(root,target):
    if not root:
        return "The BT does not exist"

    else:
        queue = []
        queue.append(root)
        while queue:
            root = queue.pop(0)
            if root.data ==   target:
                return "success"     

            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)   

        return "Not found"                   






# preorder(newBT)
# inorder(newBT)
# postorder(newBT)
# levelorder(newBT)
print(search_BT(newBT,"ta"))

