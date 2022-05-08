from node import Node


def create_list_leaf(dict):
    list_node = []
    for k in dict.keys():
        proba = dict[k]
        list_node.append(Node(k, proba))
    return list_node


def insert_node(l_nodes, node):
    if len(l_nodes) == 0:
        l_nodes.append(node)
        return l_nodes
    for i in range(len(l_nodes)):
        if node.proba <= l_nodes[i].proba:
            l_nodes.insert(i, node)
            return l_nodes
        else:
            l_nodes.append(node)
            return l_nodes


def create_huffman_tree(dict_freq):
    nodes = create_list_leaf(dict_freq)
    while len(nodes) > 1:
        l_child = nodes[0]
        l_child.code = 0
        nodes.pop(0)
        r_child = nodes[0]
        r_child.code = 1
        nodes.pop(0)
        father = Node('\0', r_child.proba + l_child.proba, l_child, r_child)
        insert_node(nodes, father)
    return nodes[0]


def coding_char(node, p, cod):
    if node.is_leaf():
        str_path = ""
        for i in p:
            str_path += str(i)
        cod[node.char] = str_path
        return
    if node.left is not None:
        p.append(node.left.code)
        coding_char(node.left, p, cod)
        p.pop(len(p) - 1)
    if node.right is not None:
        p.append(node.right.code)
        coding_char(node.right, p, cod)
        p.pop(len(p) - 1)


def get_coding(root):
    path = []
    coding = {}
    coding_char(root, path, coding)
    return coding


def huffman_coding(text, codage):
    compressed_text = ""
    for char in text:
        compressed_text += codage[char]
    return compressed_text


def bits_avarage(coding, freq):
    sum = 0
    n = 0
    for char in freq:
        n += freq[char]
    for char in coding:
        sum += len(coding[char])*freq[char]
    return sum / n