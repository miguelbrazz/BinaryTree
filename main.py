from arvore import ArvoreBinaria, ArvoreNode

#       '+'
#    /       \
#  'a'       '*'
#           /   \
#         'b'   '-'
#              /   \
#            '/'   'e'
#           /   \
#         'c'   'd'

#   (a + (b * ((c/d) - e)))


if __name__ == "__main__":
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