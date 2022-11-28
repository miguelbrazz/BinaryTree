import random
from arvore import BinarySearchTree

random.seed(66)

values = random.sample(range(1, 100), 38)

bst = BinarySearchTree()
for v in values:
    bst.insert(v)

bst.inorder_traversal()