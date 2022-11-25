from arvore import ArvoreBinaria, ArvoreNode

def inorder_example_tree():
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
    return arvore
    # arvore.simetric_traversal()
    # print()

    #      '+'
    #    /     \
    #  'a'      '*'
    #          /   \
    #        'b'    '-'
    #              /    \
    #            '/'    'e' 
    #           /   \
    #         'c'   'd'

    # (a + (b * ((c/d) - e)))

# Percurso em Pós-Ordem:
def postorder_example_tree():
    arvore = ArvoreBinaria()
    n1 = ArvoreNode('M')
    n2 = ArvoreNode('I')
    n3 = ArvoreNode('G')
    n4 = ArvoreNode('U')
    n5 = ArvoreNode('E')
    n6 = ArvoreNode('L')
    n7 = ArvoreNode('B')
    n8 = ArvoreNode('R')
    n9 = ArvoreNode('A')
    n0 = ArvoreNode('Z')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    arvore.root = n0
    return arvore
    
    
if __name__ == "__main__":
    arvore = postorder_example_tree()
    print("Percurso em pós ordem:")
    arvore.postorder_traversal()
    print("Altura:", arvore.height())