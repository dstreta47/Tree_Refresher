class TreeNode:
    def __init__(self,data, children=[]):
        self.data = data
        self.children = children
    
    def __str__(self,level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret +=child.__str__(level+1)
        return ret

    def addchild(self,TreeNode):
        self.children.append(TreeNode)    

tree = TreeNode('Deepti', [])
deep = TreeNode('Deepti1',[])
deep2 = TreeNode('Deepti2',[])
tree.addchild(deep)
tree.addchild(deep2)  
print(tree)      
