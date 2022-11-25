

class ArvoreNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def __str__(self):
        return str(self.data)


class ArvoreBinaria:
    def __init__(self, data=None):
        if data:
            node = ArvoreNode(data)
            self.root = node
        else:
            self.root = None
    
    
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')


    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)
    
    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1



if __name__ == "__main__":
    # arvore = ArvoreBinaria(7)
    # arvore.root.left = ArvoreNode(18)
    # arvore.root.right = ArvoreNode(14)

    # print(arvore.root)
    # print(arvore.root.right)
    # print(arvore.root.left)

    arvore = ArvoreBinaria()
    n1 = ArvoreNode('a')
    n2 = ArvoreNode('+')
    n3 = ArvoreNode('*')
    n4 = ArvoreNode('b')
    n5 = ArvoreNode('-')
    n6 = ArvoreNode('/')
    n7 = ArvoreNode('c')
    n8 = ArvoreNode('d')
    n9 = ArvoreNode('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    arvore.root = n2
    arvore.simetric_traversal()
    print()