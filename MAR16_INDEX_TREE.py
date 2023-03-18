
with open("input.txt","r") as ef:
    values=ef.readlines()
    for i in range(len(values)):
        values[i]=int(values[i],base=16)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root

def create_binary_tree(values):
    root = None
    for val in values:
        root = insert(root, val)
    return root

def get_depth(root):
    if root is None:
        return 0
    else:
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        return max(left_depth, right_depth) + 1

def get_width(root, level):
    if root is None:
        return 0
    if level == 1:
        return 1
    else:
        return get_width(root.left, level - 1) + get_width(root.right, level - 1)


root = create_binary_tree(values)
depth = get_depth(root)
width = max(get_width(root, i) for i in range(1, depth+1))
#print(depth)
#print(width)
print(depth*width)
